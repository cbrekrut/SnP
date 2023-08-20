def multiply_numbers(inputs):
    result = 1

    for char in inputs:
        if char.isdigit():
            digit = int(char)
            result *= digit

    return result

input_string = "Hello12345World"
product = multiply_numbers(input_string)
print(product)  # Вывод: 120 (1 * 2 * 3 * 4 * 5)
