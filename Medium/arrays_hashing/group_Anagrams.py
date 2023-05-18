"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""


class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [word]
            else:
                hashmap[sorted_word].append(word)
        return hashmap.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))



        
        
        
        

    