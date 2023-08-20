import re

def count_words(string):
    words = re.findall(r'\b\w+\b', string.lower())  
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


result1 = count_words("A man, a plan, a canal -- Panama")
print(result1)
# Вывод: {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}

result2 = count_words("Doo bee doo bee doo")
print(result2)
# Вывод: {"doo": 3, "bee": 2}

#Вариант 2

def count_words(string):
    words = string.lower().split()
    word_count = {}

    for word in words:
        word = word.strip(".,!?")  
        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


result1 = count_words("A man, a plan, a canal -- Panama")
print(result1)
# Вывод: {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}

result2 = count_words("Doo bee doo bee doo")
print(result2)
# Вывод: {"doo": 3, "bee": 2}






