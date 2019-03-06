#!/usr/bin/python3
# Description: example binary search for Python 3
# Author: Ross White 2019

import math

def binary_search(your_list, search_term):
    low = 0
    high = len(your_list) - 1

    while low <= high:
        # Divide number of entries in list in half and round up to
        # nearest integer
        mid = math.ceil((low + high) / 2)
        guess = your_list[mid]

        if guess == search_term:
            return mid
        if guess > search_term:
            high = mid - 1
        else:
            low = mid + 1
    return "Not found in list"


my_list = [1, 3, 5, 7, 9, 14, 18, 22, 30]

print(binary_search(my_list, 3))
print(binary_search(my_list, 16)) # 16 isn't in our list

name_list = ['andre', 'beth', 'charlie', 'david', 'james', 'katherine', 'leslie' \
             'otto', 'sara', 'thomas', 'valerie', 'zaphod']

print(binary_search(name_list, 'valerie'))
