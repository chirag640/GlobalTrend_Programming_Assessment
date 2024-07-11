def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

print(arithmetic_operation(10, 5, '+')) 
print(arithmetic_operation(10, 5, '/'))  
print(arithmetic_operation(10, 0, '/'))  
