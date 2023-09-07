def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    mid = len(arr)//2
    right = merge_sort(arr[mid:])
    left = merge_sort(arr[:mid])

    merged = []
    i=j=0

    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    while i<len(left):
        merged.append(left[i])
        i+=1
    while j < len(right):
        merged.append(right[j])
        j+=1


    return merged

arr = [6,10,1,100,27,9]
print(merge_sort(arr))