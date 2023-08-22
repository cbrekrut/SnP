def coincidence(input_list=None, input_range=None):
    if input_list is None or input_range is None:
        return []

    result = []
    for item in input_list:
        if isinstance(item, (int, float)) and item >= input_range.start and item < input_range.stop:
            result.append(item)
    
    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))             #Выведет => [3, 4, 5]
print(coincidence())                                         #Выведет => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) #Выведет => [1, 2, 2.5]

