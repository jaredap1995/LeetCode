"""You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

"""

input =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
infix=((10*(6/((9+3)* -11)))+17)+5


class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char.lstrip('-').isdigit():  
                val = int(char)
                stack.append(val)
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if char == '+':
                    stack.append(val1 + val2)
                elif char == '-':
                    stack.append(val1 - val2)
                elif char == '*':
                    stack.append(val1 * val2)
                elif char == '/':  # division operation
                    stack.append(int(val1 /val2))  
        return stack[0]
    

print(Solution().evalRPN(input))

"""This problem requires a basic understanding of RPN which was new for me however can be pretty simply solved
you manually perform the operations across the list like a for loop. Once you understand that,
it is basically jus implementing that in code.

Basic premise is iterate over numbers and add them to stack. When an operator is encountered, take the last two digits added 
to stack (last in first out) and perform the operation on them. Then add the result back to the stack.

The code is simple enough and follows that logic. The only thing to note is the division operation and the val2
and val1 because we are assigning val1 and val2 according to the pop operation. When we first use .pop that 
corresponds with stack[-1] and the second pop corresponds with stack [-2] so we need to use the appropraite 
val1 and val2 for the subtraction and divsion. The division operation uses int to truncate to zero, meaning you cut off
the digits after the decimal. Example: 2.7 = 2 after you slice off the 7."""





