"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

lists = [[1,2,4], [1,3,4], [2,6]]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        # Edge cases
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next
    
"""
Here we are using a recursive call to split down the list to its base components 
and then merging each linked list. It is a clever solution and the code is relatively 
striaghtforward.

Split the list into two as with a binary search algorithim.
Call the function on itself to split the left and right halves smaller and smaller.
the merge function will be called on the smallest components and then returned back up.


"""




