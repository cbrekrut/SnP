def max_odd(array):
    max_odd_value = None

    for num in array:
        if num % 2 != 0:
            if max_odd_value is None or num > max_odd_value:
                max_odd_value = num

    return max_odd_value

if __name__ == "__main__":
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9.0, 10]
    result = max_odd(my_array)
    print(result)  # Выведет: 9

    my_array2 = [2, 4, 6, 8, 10]
    result = max_odd(my_array2)
    print(result)  # Выведет: None
