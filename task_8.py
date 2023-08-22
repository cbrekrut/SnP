def multiply_numbers(inputs=None):  # Добавил аргумент по умолчанию
    if inputs is None or not isinstance(inputs, (str, int, float, list)):
        return None
    
    if isinstance(inputs, (int, float)):
        inputs = str(inputs)
    elif isinstance(inputs, list):
        inputs = ''.join(map(str, inputs))

    result = 1
    for char in inputs:
        if char.isdigit():
            digit = int(char)
            result *= digit
    
    return result if result != 1 else None


input_string = "Hello12345World"
product = multiply_numbers([input_string])
print(product)  # Вывод: 120 (1 * 2 * 3 * 4 * 5)
