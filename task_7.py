def combine_anagrams(words_array):
    anagram_dict = {}

    for word in words_array:
        sorted_word = ''.join(sorted(word.lower()))

        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    grouped_anagrams = list(anagram_dict.values())
    return grouped_anagrams


words = ["listen", "silent", "enlist", "tea", "eat", "apple"]
anagram_groups = combine_anagrams(words)
print(anagram_groups)
# Вывод: [['listen', 'silent', 'enlist'], ['tea', 'eat'], ['apple']]

anagram_groups = combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
     "creams", "scream"])
print(anagram_groups)
# Вывод: [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]
