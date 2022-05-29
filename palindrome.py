def is_palindrome(word):
    ''' To know if a word is palindrome or no'''
    word = word.lower()
    return word == word[::-1]

print(is_palindrome('radar'))
print(is_palindrome('DannyBarajas'))
