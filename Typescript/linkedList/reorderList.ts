class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val: number, next: ListNode | null){
        val = (val === undefined ? 0 : val)
        next = (next === undefined ? null : next)
    }
}

var reorderList = function(head: ListNode | null): ListNode {
    // Trvaerse whole list and find end
    let fast = head.next
    let l = 0
    let slow = head
    while (fast && fast.next !== null){
        fast = fast.next.next
        slow = slow.next
    }

    // Flip second half
    let cur = slow
    let end = null
    while (cur){
        let next = cur.next
        cur.next = end
        end = cur
        cur = next
    }

    // Trvarse starting from head again, alternating between first_half and second_half
    let first_half = head
    let second_half = end
    while (first_half){
        let tmp1 = first_half.next; let tmp2 = second_half.next
        first_half.next = second_half
        second_half.next = tmp1
        first_half = tmp1; second_half = tmp2
    }
}