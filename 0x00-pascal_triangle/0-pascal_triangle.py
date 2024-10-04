#!/usr/bin/python3
"""
0-main
"""
def pascal_triangle(n):
    """
    Print the triangle
    """
    if n <= 0:
        return []
    if n == 2:
        return [[1], [1, 1]]
    all_list = [[1], [1, 1]]
    i = 2
    while i < n :
        j = 0
        my_list = []
        while j < len(all_list[i-1]):
            if j == 0:
                my_list.append(all_list[i-1][j])         
            if j + 1 < len(all_list[i-1]):
                sum = all_list[i-1][j] + all_list[i-1][j+1]
                my_list.append(sum)
            j += 1
        my_list.append(all_list[i-1][j-1])
        all_list.append(my_list)
        my_list = []
        i += 1
    return all_list
