# -*- coding: utf-8 -*-
"""
Code challange #2 - Palindrome identifier: 

Write Python function that checks if a given word or phrase is a palindorme.

Input: string value 
Output: Boolean
Ignore case
Only consider letters (a-z)
"""
import re

def is_palindrome(phrase):
    
    # phrase = "".join(phrase)
    phrase = re.sub(r'[^a-zA-Z]+', '', phrase).lower()
    begging = phrase[:len(phrase)//2]
    
    return phrase.endswith(begging[::-1])

def is_palindrome_1(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


if __name__ == '__main__':
    # print(is_palindrome("Go hang a salami, I'm a lasagna hog.")) #[Finished in 101ms]
    print(is_palindrome_1("Go hang a salami, I'm a lasagna hog.")) #[Finished in 93ms]
    
    # print(is_palindrome("level"))
    # print(is_palindrome("hello world"))


