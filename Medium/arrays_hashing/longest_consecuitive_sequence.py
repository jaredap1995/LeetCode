"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""


"""Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""

nums=[9,1,4,7,3,-1,0,5,8,-1,6]

class Solution_mine_incorrect(object): ###My answer
    def longestConsecutive(self, nums):
        new_nums=set(nums)
        counter=0
        for num in nums:
            if num-1 in nums:
                pass
            else:
                while num+counter in new_nums:
                    counter+=1
        return counter
    


class Solution(object):
    def longestConsecutive(self, nums):
        new_nums = set(nums)
        longest_sequence = 0

        for num in new_nums:
            if num - 1 not in new_nums:
                counter = 1
                while num + counter in new_nums:
                    counter += 1
                longest_sequence = max(longest_sequence, counter)
        
        return longest_sequence


print(Solution().longestConsecutive(nums))

"""This solution works by creating a set from the list of nums. Creates a set first because
we don't want to iterate iver multiple of the same number because only one can be the 
start of a new sequence. We start a counter for longest seqeuence.

We iterate over the set and for each number in the set we check if the number-1 is in the set,
this is because if the number-1 is in the set then it is not the beginning of a sequence.
When we find a num-1 that is not in the set, we know the number we are on is the beginning of the 
seqeunce so we begin the counter. The counter starts at one to increment seqeuntially.

While num+counter in set checks if the number immediately after the current number is also in the set
if so, we increment the counter by 1 to chekc if the next number is also in the set. 
When we reach the end of the current seqeunce we set it equal to longest seqeunce if its the 
first seqeunce in the set we mapped, otherwise we take the max between longest seqeunce and 
counter."""

            
                    