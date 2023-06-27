"""
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. 

If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a,b = headA, headB
        while ( a != b ):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
    

"""
Solution Explained:

Traverse both lists fully and once each linked list is traversed we switch to the other list 
since the length of linked list a+b will be equal to b+a, the intersection will occur when
a==b

"""