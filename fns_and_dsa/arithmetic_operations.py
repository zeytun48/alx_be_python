# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the given operation.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float/str: The result of the operation or an error message if the operation is invalid.
    """
    # Handle addition
    if operation == 'add':
        return num1 + num2
    # Handle subtraction
    elif operation == 'subtract':
        return num1 - num2
    # Handle multiplication
    elif operation == 'multiply':
        return num1 * num2
    # Handle division with zero division error handling
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    # Return an error message if the operation is not valid
    else:
        return "Error: Invalid operation"

