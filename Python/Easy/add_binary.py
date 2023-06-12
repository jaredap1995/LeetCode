"""Given two binary strings a and b, return their sum as a binary string."""

class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
a="11"
b="1"
print(Solution().addBinary(a, b))

print(int(a, 2))

"""Basics of binary math. Binary is a base two operation like typically we perform base 10 operations.
So in the first column to the right most position it is a reference to the number of ones,
much like in base 10 if we the number 55, it would be 5 tens and 5 ones. In binary, we have 0 ones or 
1 one. The second column to the left then is how many twos we have, the third dolumn is how many 4's and so on.
So in the example above, we have 1 one, 1 two, and 0 fours. So the number is 3. That is the solution
to int(a, 2) where a is 11. We add 3+1 in the example above and get 4. We then convert 4 to binary.
The 'bin' operator is a Python built in function that converts a number to binary. The [2:] is a slice 
that removes the 'ob' which is automatically added on to the beginning of the binary number."""

