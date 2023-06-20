"""

A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for 
the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, 
or null if it does not point to any node.
Your code will only be given the head of the original linked list.

"""


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        # 1. Create a copy of each node and insert it between the original node and the next node
        # 2. Copy the random pointers
        # 3. Restore the original list and extract the copy list

        # Step 1 
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next # setting new node next and val to value of current node
            curr.next = new_node #placing new_node after current node
            curr = curr.next.next #moving to next node in original list which is now curr.next.next

        # Step 2
        curr = head #reassignment and iterating over new list works here because with the linked list data structure when we modify curr we modify the original head
        #So when we set 'head' to curr we are setting head to the new list
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
                curr = curr.next.next
            else:
                curr=curr.next.next
        
        # Step 3
        curr = head
        copy_head = head.next #Begining of copy list
        copy_curr = copy_head
        while curr:
            curr.next = curr.next.next #reassign to original list
            if copy_curr.next: # Meaning if copy list next is not None
                copy_curr.next = copy_curr.next.next #Skipping over values of original
            curr = curr.next #reassign curr to value in original list because we already reordered in first line of while loop
            copy_curr = copy_curr.next #Same thing as above but for new list

        return copy_head
    
