def sort_list(lst):
    if not lst:
        return []
    
    min_val = min(lst)
    max_val = max(lst)

    min_indices = [i for i, value in enumerate(lst) if value == min_val]
    max_indices = [i for i, value in enumerate(lst) if value == max_val]

    if min_val == max_val:
        min_indices.pop()
    
    for index in min_indices:
        lst[index] = max_val
    for index in max_indices:
        lst[index] = min_val
    
    lst.append(min_val)
    
    return lst


print(sort_list([]))             #Выведет => []
print(sort_list([2, 4, 6, 8]))   #Выведет => [8, 4, 6, 2, 2]
print(sort_list([1]))            #Выведет => [1, 1]
print(sort_list([1, 2, 1, 3]))   #Выведет => [3, 2, 3, 1, 1]