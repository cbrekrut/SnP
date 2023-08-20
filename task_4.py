def sort_list(lst):
    if not lst:
        return []

    min_val = min(lst)
    max_val = max(lst)
    min_idx = lst.index(min_val)
    max_idx = lst.index(max_val)

    lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]

    lst.append(min_val)

    return lst


my_list = [3, 7, 2, 10, 5]
sorted_list = sort_list(my_list)
print(sorted_list)  # Вывод: [3,7,10,2,5,2]
