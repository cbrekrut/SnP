import re

def is_palindrome(string):
    cleaned_string = re.sub(r'[^\w]', '', string)

    cleaned_string = cleaned_string.lower()
    return cleaned_string == cleaned_string[::-1]


print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))                        # True
print(is_palindrome("hello"))                          # False
print(is_palindrome("Was it a car or a cat I saw?"))   # True


def is_palindrome(string):
    def remove_punctuations(s):
        return ''.join(char for char in s if char.isalnum())
    
    cleaned_string = remove_punctuations(string)
    cleaned_string = cleaned_string.lower()
    return cleaned_string == cleaned_string[::-1]


print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))                        # True
print(is_palindrome("hello"))                          # False
print(is_palindrome("Was it a car or a cat I saw?"))   # True
