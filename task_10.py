def count_words(string):
    words = string.lower().split()
    word_count = {}
    
    for word in words:
        word = word.strip('.,!?-')
        
        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    return word_count

# Тесты
print(count_words("A man, a plan, a canal -- Panama"))  # {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}
print(count_words("Doo bee doo bee doo")) 
    

