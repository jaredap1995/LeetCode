var watchedVideosByFriends = function(watchedVideos, friends, id, level) {
    // Run a BFS starting with "id" keeping track of both the cur_node and the level
    // Create a graph object that goes graph[node]=friends
    let n = friends.length
    let graph = new Array(n).fill(0).map(() => [])
    for (let i = 0; i<n; i++){
        graph[i].push(...friends[i])
    }
    // We can access the watchedVideos with the index later on



    // cur_node, level
    let queue = [[id, 0]]
    let visited = new Set([id])
    let friends_at_levl = []

    while (queue.length) {
        let [cur_node, cur_level] = queue.shift()
        if (cur_level === level){
            friends_at_levl.push(cur_node)
        }
        else if (cur_level < level) {
            for (const neighbor of graph[cur_node]) {
                if (!visited.has(neighbor)){
                    visited.add(neighbor)
                    queue.push([neighbor, cur_level+1])
                }
            }
        }
    }

    // Flatten array of videos
    const allVidoes = [].concat(...friends_at_levl.map(friend => watchedVideos[friend]))
    console.log(allVidoes)

    const videosCount = allVidoes.reduce((acc, video) => {
        acc[video] = (acc[video] || 0) + 1
        return acc
    }, {})

    const sortedVideos = Object.keys(videosCount).sort((a,b) => {
        if (videosCount[a] !== videosCount[b]){
            return videosCount[a] - videosCount[b] // sorts by freqeuncy first
        }

        return a.localeCompare(b) // sort alphabetically otherwise
    })
    
    return sortedVideos
}


watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]] 
id = 0
level = 1

watchedVideosByFriends(watchedVideos, friends, id, level)