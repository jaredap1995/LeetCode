"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i]+1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
    

digits = [1,9]
print(Solution().plusOne(digits))

digits=[9]
print(Solution().plusOne(digits))


"""Solution works by establishing a for loop that iterates over the length of digits-1
(length of the index) but in reverse order at a step of 1 using range(len(digits)-1, -1, -1).
If the digits[i] is not 9 then we can sinmply incrmeent and retuirn which breaks us out of teh for loop.
otherwise we need to set digits[i] to 0 because once we increment from 9 a new seqeuence begins,
we continue this for each element in the list until we reach the end of the list.
If we had a list of only 9's in the list we add a [1] to the beginning, otherwise the next
iteration would add the correct value."""