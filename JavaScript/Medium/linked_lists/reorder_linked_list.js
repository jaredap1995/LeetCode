

  function ListNode(val, next) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
 }
 
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    let arr=Array();
    let current=head;
    let length=0;

    while (current){
        arr.push(current);
        current=current.next;
        length++
    };
    
    let left = 0
    let right = length-1
    let last=head

    while (left<right){
        arr[left].next=arr[right]
        left++

        if (left===right){
            last=arr[right]
            break
        };

        arr[right].next=arr[left];
        right--;

        last=arr[left]
    };

    if (last){
        last.next=null;
    };
};