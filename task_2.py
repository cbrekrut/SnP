def coincidence(lst, r):
    if not lst or not r:
        return []

    result = [num for num in lst if num in r]
    return result

if __name__ == "__main__":
    my_list = [1, 5, 10, 15, 20]
    my_range = range(5, 15)

    result = coincidence(my_list, my_range)
    print(result)  # Выведет: [5, 10]

    result = coincidence(my_list, None)
    print(result)  # Выведет: []

    result = coincidence(None, None)
    print(result)  # Выведет: []
