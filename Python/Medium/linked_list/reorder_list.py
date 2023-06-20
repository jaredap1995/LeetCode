"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        arr=[]
        cur,length=head,0

        while cur:
            arr.append(cur)
            cur,length=cur.next, length+1 #length=len
        
        left,right = 0,length-1 #length-1 is index positions
        last=head #Setting last equal to the head (beginning of initial)

        while left<right:
            arr[left].next=arr[right] #The order here of the left/right increments matters
            left+=1 #Have to have left first

            if left==right:
                last=arr[right]
                break

            arr[right].next=arr[left]
            right-=1

            last=arr[left]

        if last:
            last.next=None

            


        
