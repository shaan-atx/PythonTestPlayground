def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple CLI Calculator")
    print("Operations: +  -  *  /")

    operation = input("Choose operation (+, -, *, /): ").strip()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        raise ValueError("Invalid operation")

    print(f"Result: {result}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
