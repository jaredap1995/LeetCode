class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

var middleNode = (head: ListNode): ListNode =>  {
    let fast: ListNode | null = head
    let i: number = 0

    while (fast.next !== null) {
        fast = fast?.next
        i ++
    }

    let mid: number = Math.ceil(i/2)
    let slow: ListNode = head
    for (let i = 0; i< mid; i++){
        slow = slow?.next
    }

    return slow


}