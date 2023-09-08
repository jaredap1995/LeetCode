def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] ==value:
            return i
    
    return -1

# Simple, basic, and slow for complex problems. (O(n))