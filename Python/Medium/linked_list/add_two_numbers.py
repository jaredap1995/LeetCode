"""

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_arrays(digits1, digits2):

        #Make sure arrays same length, pad with zeros
        while len(digits1)<len(digits2):
            digits1.append(0)
        while len(digits2)<len(digits1):
            digits2.append(0)

        carry=0 #Holds carry value, gets adjusted if value added up is greater than 10
        result=[] 

        for i in range(len(digits1)):
            total=digits1[i]+digits2[i]+carry
            if total>=10:
                carry=1
                total-=10
            else: carry=0
            result.append(total)

        #Deal with leftiover carry
        if carry !=0:
            result.append(carry)

        return result

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        digits1=[]
        digits2=[]

        trav1=l1
        trav2=l2

        #Traverse list1 and get values
        while trav1.next is not None:
            digits1.append(trav1.val)
            trav1=trav1.next
        digits1.append(trav1.val)

        #Traverse list2 and get values
        while trav2.next is not None:
            digits2.append(trav2.val)
            trav2=trav2.next
        digits2.append(trav2.val)

        # digits1.reverse()
        # digits2.reverse()

        test=add_arrays(digits1, digits2)
        
        dummy_head=ListNode(0)
        ptr=dummy_head
        for num in test:
            ptr.next=ListNode(num)
            ptr=ptr.next


        return dummy_head.next
    


l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

s=Solution()
print(s.addTwoNumbers(l1,l2))




