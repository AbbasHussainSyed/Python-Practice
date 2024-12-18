# Problem: Implement exponential search to find target element in a sorted array
# Example array: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# If target = 14, return its index (6)
# If target not found, return -1

def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i = i * 2

    return binary_search(arr, target, i // 2, min(i, len(arr) - 1))


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(exponential_search(arr, 14))  # Should print 6
print(exponential_search(arr, 10))  # Should print 4
print(exponential_search(arr, 21))  # Should print -1
