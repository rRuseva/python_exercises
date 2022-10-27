# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:42:32 2022

Thechical interview Tasks

@author: Radi
"""

numbers = [1,3,5,4,6,4,6,7,9,10,11,12,13]
numbers2 = [1,2,3,4,5,5]

def isSet(numbers):
    for i in numbers[:-1]:
        if numbers[i] in numbers[i+1:]:
            return False
    return True    

# print(isSet(numbers))
# print(isSet(numbers2))

def isPalindorome(text):
    
    n = len(text)//2
    substr = text[:n]
    substr = substr[::-1]
    # if text[:n] == text[::-1]:
    #     return True
    if text.endswith(substr):
        return True
    else: 
        return False
    
print(isPalindorome("abcddcba"))

even_numbers = [x for x in numbers if x%2 == 0 ]
print(even_numbers)