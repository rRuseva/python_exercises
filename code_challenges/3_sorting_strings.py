# -*- coding: utf-8 -*-
"""
Code challange #3 - Sorting strings: 

Write Python function that sorts the words in a string.

Input: string of words separated by spaces
Output: string of words sorted alphabetically
Ignore case
"""

def sort_words(phrase):
    phrase = phrase.lower().split(" ")
    phrase.sort()
    return  ' '.join(phrase)

def sort_words2(phrase):
    phrase = phrase.split(" ")
    return  ' '.join(sorted(phrase, key = str.casefold))

def sort_words3(input):
    return ' '.join(sorted(input.split(), key = str.casefold))

if __name__ == '__main__':
    # print(sort_words("banana ORANGE apple")) # [Finished in 91ms]
    print(sort_words2("banana ORANGE apple")) # [Finished in 79ms]
    # print(sort_words3("banana ORANGE apple"))  # [Finished in 87ms]

