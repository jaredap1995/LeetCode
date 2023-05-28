"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""


class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens.append(p)
            return parens
        return generate('', n, n)



"""This problem """