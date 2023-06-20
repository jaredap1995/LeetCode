var reverseList = function(head) {
    let prev = null;
    let current = head;
    let next = null;

    while (current !== null) {
        next = current.next; // save the next node
        current.next = prev; // reverse the link
        prev = current; // move prev one step ahead
        current = next; // move current one step ahead
    }

    return prev; // at the end of the loop, prev will be the new head
};
