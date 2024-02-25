var solutiuon = function(n,firstPerson, meetings) {
    let graph = new Array(n).fill(0).map(() => [])
    for (const[n1,n2,time] of meetings){
        graph[n1].push([n2,time])
        graph[n2].push([n1,time])
    }

    let heap = new MinpriorityQueue({ priority: x=> x[0]})
    heap.enqueue([0,0])
    heap.enqueue([0,firstPerson])
    let res = new Set()

    while (heap.size()){
        let [time, cur] = heap.dequeue().element;

        if (!res.has(cur)){
            res.add(cur)
        } else {
            continue
        }

        for (const [neighbor, meetingTime] of graph[cur]){
            if (meetingTime >= time){
                heap.enqueue([meetingTime, neighbor])
            }
        }
    }

    return Array.from(res)
}