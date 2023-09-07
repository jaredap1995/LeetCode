def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = arr[len(arr)//2]
    left = [x for x in arr if x < mid]
    middle = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]

    return quick_sort(left) + middle + quick_sort(right)

arr = [6,10,1,100,27,9]
print(quick_sort(arr))