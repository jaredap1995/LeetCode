"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""

class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [sorted_hashmap[i][0] for i in range(k)]
    

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums,k))


"""Again, given that this problem requires comparing each element in a list to
every other element a nested loop could be used, which means a hashmap should be used.
We iterate over every number, add the number as a key, and then increment the freqeuncy of the number
as the value if teh number is already present in the hasmap.
We then sort the hasmap by passing the hasmpa to 'sorted' which takes an iterable.
Hashmap.items returns a list of tuples (iterbale), we then use key=lambda x: x[1] to sort the list of tuples by the second 
element in each tuple. This works because sorted is being applied to each element to understand how to sort the list.
Revese=true returns it in order of most frequent to least frequent. So in the example above the output
looks oike [(1, 3), (2, 2), (3, 1)].

Then we use a list comprehension to iterate over the list k times (the desired number of outputs) and return
the number at index [0] of each tuple which corresponds with the keys which correspond with the 
original values in nums."""
    

