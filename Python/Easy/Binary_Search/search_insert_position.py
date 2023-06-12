""""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

#Quick Binaryy search example to set the tone for writingn and aalgorithim with 0(log n) runtime complexity
def binary_search(arr,x):
    low=0
    high=len(arr)-1
    mid=0

    while low<=high:

        mid=(high+low)//2

        if arr[mid]<x:
            low=mid+1

        elif arr[mid] >x:
            high=mid-1

        else:
            return mid
        
    return low


# arr=[1,2,3,4,5,6,7,8,9,10]
# x=7
# print(binary_search(arr,x))

nums = [1,3,5,6]
target = 5
print(binary_search(nums,target))

"""This solution works by creating a binary search which splits the array into two halves 
and subsequently scans the halves depending on if the value of x is greater or less than tghe midpoints of the array.
It bases the logic on, if x is less than mid point, then we know x is in lower half,
same is true for greater half. We repeat this process until we find value of x or we reach the index where value of x should be.



This uses a O(logn) complexity if we double the size of the array, it only adds 
one more step ( a constant amount og time) to the algorithim."""
