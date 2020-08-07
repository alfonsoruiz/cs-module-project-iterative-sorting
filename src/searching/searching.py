def linear_search(arr, target):
    # Your code here
    for index, element in enumerate(arr):
        if element == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    high = len(arr) - 1
    low = 0

    while low <= high:
        middle = (low + high) // 2

        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return -1  # not found
