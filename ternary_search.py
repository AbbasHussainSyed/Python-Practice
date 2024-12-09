# Input array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Target = 7
# Should return index 6

def ternary_search(arr, val, low, high):
    if low > high:
        return -1

    mid1 = low + (high - low) // 1/2
    mid2 = low + (high - low) // 2/3

    if arr[mid1] == val:
        return mid1
    elif arr[mid1] > val:
        return ternary_search(arr, val, low, mid1-1)
    else:
        return ternary_search(arr, val, mid1+1, high)

    
