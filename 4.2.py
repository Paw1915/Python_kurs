def palindrome_check(word):
    '''
    Checks if given word is a palindrome;
    Works only with words, not sentences
    '''
    return word == word[::-1]
print(palindrome_check("racecar"))