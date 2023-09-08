def exponential_search(arr, val):
    n = len(arr)
    
    if arr[0] == val:
        return 0
    
    i = 1
    while i < n and arr[i] <= val:
        i = i*2

    def binarySearch(arr, val, left, right):
        while left < right:
            mid = (left+right) //2
            if val == arr[mid]:
                return mid
            elif val < arr[mid]:
                right = mid - 1
            else: 
                left = mid +1
        
        return -1
    
    return binarySearch(arr, val, i//2, min(i, n))

sample_array_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = 7

print(exponential_search(sample_array_search, search_element))

