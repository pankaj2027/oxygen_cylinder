# 1. Write a program to flatten the nested list.
# Input:- [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]
# Output:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

final_list = []

def remove_nested(arr):
    for i in arr:
        if type(i) == list:
            remove_nested(i)
        else:
            final_list.append(i)



arr= [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]
remove_nested(arr)
print( final_list)