def solution(head):
    cur = head
    end = None

    while cur is not None:
        next_ = cur.next
        cur.next = end
        end = cur
        cur = next_

    return end

