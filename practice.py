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



# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible,
#  containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    new = a1 + a2
    result = []
    for x in new:
        if x not in result:
            result.append(x)
    result.sort()
    return ''.join(result)

# Take 2 strings s1 and s2 including only letters from ato z.
#  Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    new = a1 + a2
    result = []
    for x in new:
        if x not in result:
            result.append(x)
    result.sort()
    return ''.join(result)


# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    compare = ['a','e','i','o','u']
    string_ = list(string_)
    new = ['1' if x.lower() in compare else x for x in string_]
    final = []
    for x in new:
        if x != '1':
            final.append(x)
    final = ''.join(final)  
    
    
    return final


# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
import string

def is_pangram(s):
    s = list(s.lower())
    s.sort()
    for i in range(len(s)-1):
        if s[i].isalpha():
            if s[i].lower() == s[i+1].lower():
                pass
            elif ord(s[i+1].lower()) - ord(s[i].lower()) == 1:
                pass
            else:
                return False
    return True

# Find the unique number (this kata)

def find_uniq(arr):

    for i in range(len(arr)): 
        if i == len(arr) - 2:
            if arr[i] == arr[i-1]:
                return arr[i+1]
            else:
                return arr[i]
        elif arr[i] == arr[i+1]:
            pass
        else:
            if arr[i] == arr[i+2]:
                return arr[i+1]
            return arr[i]



# Complete the solution so 
# that it splits the string into pairs
#  of two characters. If the string 
#  contains an odd number of characters 
#  then it should replace the missing second character of the final pair with an underscore ('_').

def solution(s):
    result = []
    if s == '':
        return []
    elif len(s) == 1:
        result.append(s[0]+'_')
        return result
    elif len(s) % 2 == 0:
        for i in range(0,len(s),2):
            result.append(s[i]+s[i+1])
        return result
    else:
        for i in range(0,len(s),2):
            if i == len(s) - 1:
                result.append(s[i]+'_')
            else:
                result.append(s[i]+s[i+1])
        return result
            

# You will be given an array of numbers. You have to sort the odd numbers in ascending 
# order while leaving the even numbers at their original positions.

def sort_array(source_array):
    copy = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            copy.append(source_array[i])
            source_array[i] = '!'
    copy.sort()
    counter = 0
    for i in range(len(source_array)):
        if source_array[i] == "!":
            source_array[i] = copy[counter]
            counter += 1
    return source_array


# Given two arrays a and b write a function
#  comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the 
#  "same" elements, with the same multiplicities (the multiplicity of a member 
#  is the number of times it appears). "Same" means, here, that the elements in b
#   are the elements in a squared, regardless of the order.

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


# is a number prime
def is_prime(num):
    if num <= 0 or num == 1:
        return False
    i = 2
    while (i <= num ** 0.5 ):
        if num % i == 0:
            return False
        i += 1
    return True


# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether 
# the two arrays have the "same" elements, with the same multiplicities (the multiplicity of
#  a member is the number of times it appears). "Same" means, here, that the elements in b are
#   the elements in a squared, regardless of the order.

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


# You will be given a number and you will need to return it as a string in Expanded Form. 

def expanded_form(num):
    num = str(num)
    result = []
    for i in range(len(num)):
        if i == len(num) - 1:
            if num[i] != '0':
                result.append(num[i])
        elif num[i] != '0':
            space_after = len(num[i+1:])
            result.append(num[i] + ('0' * space_after))
    return ' + '.join(result)