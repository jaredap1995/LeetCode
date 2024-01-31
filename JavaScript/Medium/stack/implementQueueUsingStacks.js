class MyQueue {
    constructor() {
        this.queue = [];
    }
}

MyQueue.push = (x) => {
    this.queue.push(x)
}

MyQueue.pop = () => {
    return this.queue.pop()
}

MyQueue.peek = () => {
    return this.queue[0]
}

MyQueue.isEmpty = () => {
    if (this.queue.length > 0) return false
    return true
}