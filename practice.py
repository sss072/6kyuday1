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


# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.    

def alphabet_position(text):
    text = list(text.lower())
    for i in range(len(text)):
        if text[i].isalpha():
            text[i] = ord(text[i]) - 96
        else:
            text[i] = '!'
    while '!' in text:
        text.remove('!')
    string_ints = [str(int) for int in text]
    return ' '.join(string_ints)
            


# Your task is to sort a given string. Each word in the string will contain a single number.
#  This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def order(sentence):
    new = sentence.split()
    result = new.copy()
    for x in new:
        word_list = list(x)
        for x in word_list:
            if x.isdigit():
                word_list.remove(x)
                result[int(x)-1] = ''.join(word_list)
    return ' '.join(result)
    
order("is2 Thi1s T4est 3a")