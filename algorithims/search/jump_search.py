import math

def jump_search(arr, val):
    n=len(arr)
    jump = math.sqrt(n)
    end=int(min(jump,n)-1)
    end=arr[end]
    prev= 0

    while end < val:
        prev = jump
        jump += math.sqrt(n)
        end=arr[int(min(jump,n)-1)]

        if prev >= n:
            return None
        
    while arr[int(prev)] < val:
        prev +=1

        if prev == min(jump, n):
            return -1
            
    if arr[int(prev)] == val:
        return int(prev)
        
    return -1
    
sample_array_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = 7

print(jump_search(sample_array_search, search_element))