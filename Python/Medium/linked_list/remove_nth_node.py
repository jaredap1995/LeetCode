"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow=head
        fast=head

        for i in range(n):
            fast=fast.next
        if not fast: #Handles edge case where n=len(head)
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next #Skips the 'next' which is the node we want to remove
        return head
    

"""
We iterate over the range of n and if fast is already none then we know that n is equal to the
length of the linked list and we return head.next.

If there is a fast.next then we continue iterating until we reach the end (fast.next=None)
also iterating slow. 

Because we started slow n steps behind fast slow.next will always sit on the node we need to remove when
we exit on fast.next==None.



"""
        
        
        





