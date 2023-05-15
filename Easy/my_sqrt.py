"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator."""

class Solution:
    def mySqrt(self, x):
        if x==1:
            return 1
        low=0
        high=x
        while low<=high:
            mid=(low+high)//2
            if mid*mid>x:
                high=mid-1
            elif mid*mid<x:
                low=mid+1
            else:
                return mid
        return high

x=8
print(Solution().mySqrt(x))

"""Soultion uses a binary search tree to squeeze the number down to its square root.
Start with a low of 0 and a high of x. Find the midpoint, in ideal case, mid*mid is equal to x, however when it is not,
it will tell us whether mid needs to be decreased or increased in order to find the squareroot."""



        




