from src.calculator import add, subtract, multiply, divide
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# UI Route
@app.route('/')
def home():
    return render_template("index.html")

# API Route
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data or 'operation' not in data or 'x' not in data or 'y' not in data:
        return jsonify({"error": "Invalid input, please provide 'operation', 'x', and 'y'"}), 400

    operation = data['operation']
    x = data['x']
    y = data['y']

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return jsonify({"error": "x and y must be numbers"}), 400

    if operation == "add":
        result = add(x, y)
    elif operation == "subtract":
        result = subtract(x, y)
    elif operation == "multiply":
        result = multiply(x, y)
    elif operation == "divide":
        result = divide(x, y)
    else:
        return jsonify({"error": "Unsupported operation"}), 400

    return jsonify({
        "operation": operation,
        "x": x,
        "y": y,
        "result": result
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
