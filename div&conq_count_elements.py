# Given an array A of n integers and a value x, count how many elements in A are strictly greater than x.
# Use a divide-and-conquer algorithm to solve the problem

def count_elements(arr, x):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1 if arr[0] > x else 0

    first_half = count_elements(arr[:len(arr) // 2], x)
    second_half = count_elements(arr[len(arr) // 2:], x)
    return first_half + second_half


arr = [2, 3, 4, 4, 9]
x = 4
result = count_elements(arr, x)
print(result)