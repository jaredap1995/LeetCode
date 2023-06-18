"""
You are given an array of integers nums, 
there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

"""
nums = [1,3,-1,-3,5,3,6,7]
k = 3

from collections import deque

# deque.index
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        if k==1:
            return nums
        
        deq=deque()

        def clean_deque(i):
            if deq and deq[0]==i-k:
                deq.popleft()

            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        max_idx=0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i]>nums[max_idx]:
                max_idx=i
        output=[nums[max_idx]]

        for i in range(k, len(nums)):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

"""We needed a data structure that respects the order of the values (dequeue works in 
this instance). You need to popleft the deqeue when you reach the end of its current range
that is determined by i-k. 

You also pop right (normal pop) when you come across a value in nums that is the new max.
This is a while loop so you continually pop until the max number index is first in the dequeu.

First for loop handles first window, second for loop handles all subsequent ones.
The i-k is only intiiated in the function when no new max value has been encountered and 
we have reached a total of iterations that is equal to 'k'.

In contrast, the while loop is always checked on every iteration, if there are only ascending
values we would never actually eneter the first if statement as at every iteration we would pop
and replace with the new highest index.

In the second for loop we also make sure to append the max value (nums[deq[0]]) because
we have passed the first window so every iteration from here on out is its own window.
"""




class Solution_mine_too_slow(object):
    def maxSlidingWindow(self, nums, k):
        start=0
        end=k
        maxes=[]
        i=0
        while i<len(nums):
            high=max(nums[start:end])
            maxes.append(high)
            i+=1
            start+=1
            end+=1
        pops_needed=k-1
        j=0
        while j<pops_needed:
            maxes.pop()
            j+=1
        return maxes
    

print(Solution().maxSlidingWindow(nums, k))

