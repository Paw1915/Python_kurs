def palindrome_check(word):
    return word == word[::-1]
print(palindrome_check("racecar"))