"""Given the head of a linked list, 
reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed."""


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy

        while head:
            group_start = head
            group_end = self.getGroupEnd(head, k)

            if group_end is None:
                break

            reversed_group = self.reverseList(head, group_end.next)
            prev_group_tail.next=reversed_group
            prev_group_tail = group_start
            head = prev_group_tail.next
        
        new_head = dummy.next
        return new_head


    def getGroupEnd (self,head,k):
        while head and k>1:
            head=head.next
            k-=1
        return head
    
    def reverseList (self, head, stop):
        prev = stop
        while head != stop:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev