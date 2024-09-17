def basic_math_operation(x, y, operation):
    """Performs a basic math operation on two numbers.

    :param x: First number
    :param y: Second number
    :param operation: Operation to perform: 'add', 'subtract', 'multiply', or 'divide'
    :return: Result of the operation
    """
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    else:
        raise ValueError("Unsupported operation")
