/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    let graph = new Array(rooms.length).fill(0)
    for (let i = 0; i<graph.length; i++){
        graph[i]=rooms[i]
        if (rooms[i]===i) {return false}
    }

    let keys = new Set()

    var DFS = (key) => {
        if (keys.has(key)){return}

        keys.add(key)
        for (const neighbor of graph[key]){
            DFS(neighbor)
        }
    }
    var sortHelper = (a,b) =>{return a-b}

    DFS(0)

    if (rooms.length==keys.size) {
        return true
    } else {
        return false}

    
};

rooms = [[1],[2],[3],[]]
console.log(canVisitAllRooms(rooms))