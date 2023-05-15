"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well."""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def deleteDuplicates(self, head):
        current=head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next=current.next.next
            else:
                current = current.next
        return head



head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)


