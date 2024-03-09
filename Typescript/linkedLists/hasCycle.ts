class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val? : number, next? : ListNode | null){
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null: next)
    }
}

var hasCycle = (head: ListNode | null): boolean => {
    let fast: ListNode | null = head
    let slow: ListNode | null = head

    while (fast && fast.next){
        fast = fast.next.next
        slow = slow.next // Added null check here
        if (slow === fast) return true
    }

    return false
}