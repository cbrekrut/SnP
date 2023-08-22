def max_odd(numbers):
    max_odd_value = None

    for item in numbers:
        if isinstance(item, (int, float)) and item % 2 == 1:  
            if max_odd_value is None or item > max_odd_value:
                max_odd_value = item
    
    return max_odd_value


print(max_odd([1, 2, 3, 4, 4]))                  #Выведет => 3
print(max_odd([21.0, 2, 3, 4, 4]))               #Выведет => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) #Выведет => 3
print(max_odd(['ololo', 'fufufu']))              #Выведет => None
print(max_odd([2, 2, 4]))                        #Выведет => None