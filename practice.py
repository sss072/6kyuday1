# The goal of this exercise is to convert a string to a new string 
# where each character in the new string is "(" if that character appears only once in the original string, or ")" 
# if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.


def duplicate_encode(word):
    word = list(word.lower())
    counter = []
    for letter in word:
        if word.count(letter) > 1:
            counter.append(')')
        else:
            counter.append('(')
    return ''.join(counter)

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
#  which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n):
    if 'count' not in locals():
        count = 0
    strr = str(n)
    if len(strr) == 1:
        return count
    else:
        result = 1
        mult_result = list(map(int, strr.strip()))
        for x in mult_result:
            result = result * x
        count += 1
        return persistence(result)
        
persistence(39)