"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

s = "()[]{}"


class Solution(object):
    def isValid(self, s):
        if s=='': return True
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i == ')' and (not stack or stack.pop() != '('):
                    return False
                elif i == '}' and (not stack or stack.pop() != '{'):
                    return False
                elif i == ']' and (not stack or stack.pop() != '['):
                    return False
        return not stack


print(Solution().isValid(s))

"""This problem focuses on a new data structure, a 'Stack.' A stack is a data structure that follows the last in first out approach and 
is well demonstrated by the parentheses, curly braces, and brackets as these must follow this logic in order to be valid.

First thing we do to solve this problem is initialize and empty stack, we then iterate over string s. We know s only has brackets, parentheses, or curly braces.
If we find an opening one, we add it to the stack, if it is a closing one, we check the most recent one added, since the only way for it to be valid is for the
last in to match the current closing charachter.

We handle a few edge cases by using 'if not stack' after the else statement in the event it is exclusively closing braces, and we handle it being only opening charachters
by retruning 'not stack' as a stack with unmatched opening chrachters would be True so we return 'not stack' to retrun False. 

Similarly, when all goes well, we would have an empty stack if everything gets popped, so when we return 'not stack' we return True"""

