import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test Home Page
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Simple Calculator" in response.data  # check HTML content

# Test Add Operation
def test_addition(client):
    response = client.post("/calculate", json={"operation": "add", "x": 10, "y": 5})
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 15

# Test Subtract Operation
def test_subtraction(client):
    response = client.post("/calculate", json={"operation": "subtract", "x": 10, "y": 5})
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 5

# Test Multiply Operation
def test_multiplication(client):
    response = client.post("/calculate", json={"operation": "multiply", "x": 4, "y": 5})
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 20

# Test Division Operation
def test_division(client):
    response = client.post("/calculate", json={"operation": "divide", "x": 20, "y": 4})
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 5

# Test Division by Zero
def test_division_by_zero(client):
    response = client.post("/calculate", json={"operation": "divide", "x": 10, "y": 0})
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == "Error! Division by zero."

# Test Invalid Operation
def test_invalid_operation(client):
    response = client.post("/calculate", json={"operation": "mod", "x": 10, "y": 2})
    data = response.get_json()
    assert response.status_code == 400
    assert "error" in data

# Test Missing Fields
def test_missing_fields(client):
    response = client.post("/calculate", json={"x": 10})
    data = response.get_json()
    assert response.status_code == 400
    assert "error" in data

# Test Non-numeric Input
def test_non_numeric_input(client):
    response = client.post("/calculate", json={"operation": "add", "x": "abc", "y": 5})
    data = response.get_json()
    assert response.status_code == 400
    assert "error" in data
