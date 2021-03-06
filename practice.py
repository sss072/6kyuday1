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

# Complete the solution so that the function will break up camel casing, 
# using a space between words.


def solution(s):
    s = list(s)
    place_holder = ''
    counter = 0
    for i in range(len(s)):
        if i == 0:
            pass
        elif s[i] == s[i].upper():
            place_holder += ''.join(s[counter:i])
            place_holder += ' '
            counter = i
    place_holder += ''.join(s[counter:])
    return place_holder

# The number 89 is the first integer with more than one digit that fulfills the property 
# partially introduced in the title of this kata. What's the use of saying "Eureka"? 
# Because this sum gives the same number.

# In effect: 89 = 8^1 + 9^2

# The next number in having this property is 135.

# See this property again: 135 = 1^1 + 3^2 + 5^3

# We need a function to collect these numbers, that may receive two integers a, b that 
# defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that 
# fulfills the property described above.

def sum_dig_pow(a, b): 
    result = []
    for x in range(a,b+1):
        x = str(x)
        counter = 1
        compare = []
        for i in x:
            compare.append(int(i) ** counter)
            counter += 1
        if sum(compare) == int(x):
            result.append(int(x))
    return result


# The input is a string str of digits. 
# Cut the string into chunks (a chunk here is a substring of the initial string) 
# of size sz (ignore the last chunk if its size is less than sz).

# If a chunk represents an integer such as the sum of the cubes of its digits is 
# divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. 
# Put together these modified chunks and return the result as a string.


# Write a function that takes an array of numbers (integers for the tests) and a target number. 
# It should find two different items in the array that, when added together, give the target value. 
# The indices of these items should then be returned in a tuple like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be 
# accepted.

# The input will always be valid (numbers will be an array of length 2 or greater, and all of the 
# items will be numbers; target will always be the sum of two different items from that array).

def revrot(strng, sz):
    if sz == 0 or sz > len(strng) or strng == '':
        return ''
    else:
        result = ''
        flag = True
        while flag:
            if len(strng) >= sz:
                checker = strng[:sz]
                strng = strng[sz:]
                final = [int(x) ** 3 for x in checker]
                if sum(final) % 2 == 0:
                    checker = checker[::-1]
                    for i in checker:
                        result += i
                else:
                    final = checker[1:]
                    final += checker[0]
                    result += final
            else:
                flag = False
        return result

# Write simple .camelCase method 
# (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. 
# All words must have their first letter capitalized without spaces.
def camel_case(string):
    string = string.split()
    if string == '':
        return ''
    for x in range(len(string)):
        string[x] = string[x].capitalize()
    return ''.join(string)



def two_sum(numbers, target):
    for x in range(len(numbers)-1):
        for y in range(x+1,len(numbers)):
            if numbers[x] + numbers[y] == target:
                return (x,y)



# Write a function which takes numbers num1 and num2 and returns 1 if there 
# is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
# If this isn't the case, return 0

def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    flag = 0
    var = 0
    for i in range(len(num1)-2):
        if num1[i] == num1[i+1] and num1[i] == num1[i+2]:
            flag = 1
            var = num1[i]
    for i in range(len(num2)-1):
        if num2[i] == var and num2[i] == num2[i+1] and flag == 1:
            return flag 
    return 0

# Write a function that accepts a string, and returns true if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)


import re
def valid_phone_number(phone_number):
    if len(phone_number) == 14:
        if phone_number[0] == '(' and phone_number[4] == ')':
            if phone_number[1].isdigit() and phone_number[2].isdigit() and phone_number[3].isdigit():
                if phone_number[6].isdigit() and phone_number[7].isdigit() and phone_number[8].isdigit():
                    if phone_number[10].isdigit() and phone_number[11].isdigit() and phone_number[12].isdigit() and phone_number[13].isdigit():
                        if phone_number[5] == ' ' and phone_number[9] == '-':
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False                
        else:
            return False
    else:
        return False
                    
# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array

def parse(data):
    total = 0
    result = []
    for x in data:
        if x == 'i':
            total += 1
        elif x == 'd':
            total -= 1
        elif x == 's':
            total = total ** 2
        elif x == 'o':
            result.append(total)
    return result

# Given a lowercase string that has alphabetic characters only and no spaces, return the highest 
# value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

import re
def solve(s):
    s = re.split('a|e|i|o|u',s)
    result = {}
    for x in s:
        result[x] = 0
        for i in x:
            result[x] += ord(i) - 96
    all_values = result.values()
    max_value = max(all_values)
    return max_value

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def number(bus_stops):
    counter = 0
    for x in bus_stops:
        counter += x[0]
        counter -= x[1]
    return counter

def divisors(integer):
    result = []
    for i in range(2,integer):
        if integer % i == 0:
            result.append(i)
    if result == []:
        return f"{integer} is prime"
    else:
        return result

# function feast(beast, dish) {
#   if (beast[0] === dish[0] && beast[beast.length - 1] === dish[dish.length - 1]) {
#     return true
# } else {
#     return false
# }
# }



# sort array by string length 
def sort_by_length(arr):
    dict = {}
    for x in arr:
        dict[x] = len(x)
    result = []
    for x in arr:
        result.append(min(dict, key=dict.get))
        del dict[min(dict, key=dict.get)]
    return result