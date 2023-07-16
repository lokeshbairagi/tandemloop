class Calculator:
    def add(self, operand1, operand2):
        return operand1 + operand2

    def subtract(self, operand1, operand2):
        return operand1 - operand2

    def multiply(self, operand1, operand2):
        return operand1 * operand2

    def divide(self, operand1, operand2):
        if operand2 != 0:
            return operand1 / operand2
        else:
            return "Error: Division by zero"


def main():
    calculator = Calculator()

    operator = input("Enter the operator (+, -, *, /): ")
    operand1 = float(input("Enter the first operand: "))
    operand2 = float(input("Enter the second operand: "))

    if operator == "+":
        result = calculator.add(operand1, operand2)
    elif operator == "-":
        result = calculator.subtract(operand1, operand2)
    elif operator == "*":
        result = calculator.multiply(operand1, operand2)
    elif operator == "/":
        result = calculator.divide(operand1, operand2)
    else:
        result = "Error: Invalid operator"

    print("Result: ", result)


if __name__ == "__main__":
    main()
