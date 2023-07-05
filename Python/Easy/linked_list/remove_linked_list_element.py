"""

Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def removeElements(self, head, val):
        while head and head.val==val:
            head=head.next #Checking edge case where first value == val
        a=head
        while a is not None:
            if a.next is not None and a.next.val==val:
                a.next=a.next.next
            else:
                a=a.next
        
        return head
    
    