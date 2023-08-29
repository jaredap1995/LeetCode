#define a function to sort values in array using selection sorting

def mysort(arr, size):
    #Iterate over the indexes in the array
    for ind in range(size):
        #Set the minimum index to the current index
        min_index = ind

        #Iterate from current index+1 to end of array
        for j in range(ind + 1, size):
            if arr[j] <arr[min_index]:
                min_index = j
            
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])

    return arr

arr = [7,4,10,112,3,9]
size = len(arr)
print(mysort(arr, size))