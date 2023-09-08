def binary_search(arr, val):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left+right)//2
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            right = mid -1
        else:
            left = mid+1
    return -1

sample_array_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = 7

print(binary_search(sample_array_search, search_element))

