"""Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""





# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        new_end=None
        current=head

        while current:
           next_node=current.next #Save what the head points to next
           current.next=new_end #Assign None as the the .next value for the first iteration (why new_list is set=None) since it is now going to be the last value in linked list
           new_end=current #Now reassign new_list to what the .next value will be for teh following iteration (the current value)
           current=next_node #Set current to the next node so current has a value and we continue

        return new_end
        


val1=ListNode(1,2)
val2=ListNode(2,3)
val3=ListNode(3,4)
val4=ListNode(4,5)
val5=ListNode(5)

head=[val1,val2,val3,val4,val5]

print(Solution().reverseList(head))
