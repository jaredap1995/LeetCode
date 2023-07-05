/**
 * @param {ListNode} head
 * @return {head}
 */

var removeElements = function (head, val) {
    while (head && head.val==val){
        head=head.next
    }
    let a = head;
    while (a != null){
        if (a.next != null && a.next.val==val){
            a.next=a.next.next;
        } else {a=a.next}
    }
    return head
};

removeE => {
    return 100+200;
};

a => 100+200;