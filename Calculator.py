# Function to perform arithmetic operations
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation choice"

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the operation choice (1/2/3/4): ")

# Perform the calculation and display the result
result = calculate(num1, num2, operation)
print("Result:", result)
