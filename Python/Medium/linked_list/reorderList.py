def solution(head):
    # Traverse with Tortoise and Hare
    fast = head.next
    slow = head

    # Whole list traversal
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # Reverse second half of linked list
    cur = slow
    end = None
    while cur:
        next_ = cur.next
        cur.next = end
        end = cur
        cur = next_
    
    # Merge the two lists
    first_half = head
    second_half = end
    while first_half:
        temp1, temp2 = first_half.next, second_half.next
        first_half.next = second_half
        second_half.next = temp1
        second_half,first_half = temp2, temp1






