#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_in_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        new_in_list[idx] = element

        length = len(new_in_list)
        return new_in_list
