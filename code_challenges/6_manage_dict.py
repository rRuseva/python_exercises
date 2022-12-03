# -*- coding: utf-8 -*-
"""
Code challange #6 - Save a dictionary: 

1) Write Python function to save a dictionary to a file.

Input: Dictionary to save , output file path
Output: text file with the saved dictionary

2) Write Python function to retrieve the dictionary

Input: File path to saved dictionary 
Output: retrieved dictionary object.

"""

def save_dict(data, file_path):
    with open(file_path,'w') as wf:
        wf.write(data)
 

def load_dict(file_path):
    with open(file_path, 'r') as rf:
        data = rf.read()
    data = data[1:-1].split(',')
    result_dict = {}
    for entry in data:
        entry = entry.split(':')
        result_dict[entry[0]] = entry[1]
    
    
    return result_dict


""" Another solution using pickle module for serialization
- serialization - It’s the process of converting an object into a byte stream that can be stored """

import pickle 
def save_dickt_pickling(data, file_path):
    with open(file_path, 'wb') as wf:
        pickle.dump(data, wf)

def load_dict_pickling(file_path):
    with open(file_path,'rb') as rf:
        return pickle.load(rf)


if __name__ == '__main__':
    test_dict = {1: 'a', 2: 'b', 3: 'c'}
    
    save_dict(str(test_dict), 'test.txt')
    
    new_data = load_dict("test.txt")
    print(type(new_data))
    
    
    save_dickt_pickling(test_dict, 'test.pickle')
    new_dict = load_dict_pickling('test.pickle')
    print(new_dict)
    print(type(new_dict))