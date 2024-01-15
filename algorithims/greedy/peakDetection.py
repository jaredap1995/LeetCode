"""
When arr has only a single peak

"""

def findPeak(arr):
    start = 0
    end = len(arr)-1

    while start < end-1:
        mid = (start + end) // 2

        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == len(arr)-1 or arr[mid+1] <= arr[mid]):
            return arr[mid]
        elif arr[mid] < arr[mid+1]:
            start = mid
        else:
            end = mid
    
    return arr[start]


arr = [1, 3, 20, 4, 1, 0, 7, 8, 9, 2]
print(findPeak(arr))


"""
Finding multiple peaks within a stream of data like an ECG

"""

def multiplePeaks(arr, window):
    peaks = []
    n = len(arr)

    for i in range(n):
        is_peak = True
        for j in range(max(0,i-window), min(n, i+window+1)):
            if i != j and arr[i]< arr[j]:
                is_peak = False
                break
        if is_peak:
            peaks.append(i)

    return peaks

arr = [1, 3, 7, 6, 4, 2, 5, 9, 8, 7]
print(multiplePeaks(arr, 2))