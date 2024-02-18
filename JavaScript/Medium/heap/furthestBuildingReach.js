import {MinPriorityQueue} from '@datastructures-js/priority-queue;'

var solution = function(heights, bricks, ladders){
    let n = heights.length
    let heap = new MinPriorityQueue({ priority: x => x})
    for (let i = 1; i<n; i++){
        let diff = heights[i] - heights[i-1];
        if (diff > 0){
            heap.enqueue(diff)
        }
        if (heap.size() > ladders){
            bricks -= heap.dequeue().element;
            if (bricks < 0) return i - 1
        }
    }

    return n-1
}