var getIntersectionNode = function(headA, headB) {
    a = headA;
    b = headB;
    while (a !== b) {
        a = !a ? headB : a.next //Translation: If a is not a (meaning null) then headB, else a.next
        b = !b ? headA : b.next
    }
    return a
};



var evenOdd = function (number){
    output = number % 2 ===0 ? 'Even' : 'Odd'
    return output
};

console.log(evenOdd(4))