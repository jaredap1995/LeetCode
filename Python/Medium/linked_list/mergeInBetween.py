# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        fast = list1
        slow = list1
        
        i = 0
        while fast.next is not None and i < b+1:
            i+= 1
            fast = fast.next

        i = 0
        while slow.next is not None and i < a:
            if i == a - 1:
                slow.next = list2
                break
            i += 1
            slow = slow.next

        while slow.next is not None:
            slow = slow.next
        slow.next = fast
            # while i <= b + 1:
            #     i += 1
            #     fast = fast.next
            # fast.next = 

        return dummy.next


        