def connect_dicts(dict1, dict2):
    def filter_and_sum_values(dictionary):
        return sum(value for value in dictionary.values())

    sum1 = filter_and_sum_values(dict1)
    sum2 = filter_and_sum_values(dict2)

    priority_dict = dict1 if sum1 > sum2 else dict2
    secondary_dict = dict2 if priority_dict is dict1 else dict1

    combined_dict = {}
    for key, value in priority_dict.items():
        if value >= 10:
            combined_dict[key] = value

    for key, value in secondary_dict.items():
        if value >= 10 and key not in combined_dict:
            combined_dict[key] = value

    sorted_combined_dict = dict(sorted(combined_dict.items(), key=lambda item: item[1]))

    return sorted_combined_dict


result1 = connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })
print(result1)  # Вывод: { "c": 11, "b": 12 }

result2 = connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })
print(result2)  # Вывод: { "d": 11, "c": 12, "a": 13 }

result3 = connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })
print(result3)  # Вывод: { "c": 11, "b": 12, "a": 15 }
