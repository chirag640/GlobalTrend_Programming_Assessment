def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result


print(divide_numbers(10, 2))  
print(divide_numbers(10, 0))  
