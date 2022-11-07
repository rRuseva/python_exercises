# -*- coding: utf-8 -*-
"""
Code challange #4 - Index items in multi dimensional list: 

Write Python function that index all items in a list. 

Input: list to search in, value to search for # example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], value = 2z
Output: list of indecies  #[[0, 0, 1], [0, 1], [1, 1]]
Lists can be multi dimensional

"""

def index_all_1(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all_1(search_list[i], item):
                indices.append([i]+index)
    return indices

def index_all(items, value):
    idxs = []
    
    for i, item in enumerate(items):
        if item == value:
            idxs.append([i])
        elif isinstance(item, list):
            if value in item:
                for index in index_all(item, value):
                    idxs.append([i]+index)
                
    return idxs

if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3] ]
    example2 = [1,2,3]
    example3 = [ [[1, 2, 3], 2, [1, 3]] ]
    
    # print(index_all(example3,2)) #[Finished in 93ms]
    # print(index_all_1(example3,2)) #[Finished in 80ms]

    # print(index_all(example,2)) #[Finished in 76ms]
    # print(index_all_1(example,2)) #[Finished in 82ms]

    print(index_all(example,[1, 2, 3])) #[Finished in 82ms]
    print(index_all_1(example,[1, 2, 3])) #[Finished in 88ms]
    
    
    