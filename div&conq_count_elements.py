# Given an array A of n integers and a value x, count how many elements in A are strictly greater than x.
# Use a divide-and-conquer algorithm to solve the problem

def count_elements(arr, x):
    if len(arr) == 0:
        return 0
    if len(arr) == 1 and arr[1] >= x:
        return 1
    else:
        first_half = count_elements(arr[:arr/2], x)
        second_half = count_elements(arr[arr/2:], x)
    return first_half+second_half

arr = []