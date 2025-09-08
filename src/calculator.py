# Simple Calculator Project in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("===== Simple Calculator =====")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {add(num1, num2)}\n")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}\n")
                elif choice == '3':
                    print(f"Result: {multiply(num1, num2)}\n")
                elif choice == '4':
                    print(f"Result: {divide(num1, num2)}\n")

            except ValueError:
                print("Invalid input! Please enter numbers only.\n")
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    calculator()
