def interpolation_search(arr, val):
    left, right = 0, len(arr)-1
    while left <= right and val >= arr[left] and val <=arr[right]:
        if left == right:
            if arr[left] == val:
                return left
            return -1
    
        pos = left + int(((right - left)/(arr[right]-arr[left])) *(val - arr[left]))
        if arr[pos] == val:
            return pos
        elif arr[pos] < val:
            left = pos + 1

        else: 
            right = pos - 1

    return -1

sample_array_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = 7

print(interpolation_search(sample_array_search, search_element))