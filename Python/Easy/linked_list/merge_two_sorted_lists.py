"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ans=ListNode()
        ptr=ans
        while list1 and list2:
            if list1.val<=list2.val:
                ans.next=ListNode(list1.val)
                list1=list1.next
            else:
                ans.next=ListNode(list2.val)
                list2=list2.next
            ans=ans.next
        while list1:
            ans.next=ListNode(list1.val)
            list1=list1.next
            ans=ans.next
        while list2:
            ans.next=ListNode(list2.val)
            list2=list2.next
            ans=ans.next
        return ptr.next

            

