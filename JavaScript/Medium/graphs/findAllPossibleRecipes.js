var solution = function(recipes, ingredients, supplies){
    let n = recipes.length
    let graph = {}
    let inDegree = {}


    var zip = (arrays) => {
        return arrays[0].map((_, i) => {
            return arrays.map((array) => array[i])
        })
    }

    zip([ingredients, recipes]).forEach(([ingredientList, recipe]) => {
        
        ingredientList.forEach((ingredient) => {
            if (!graph[ingredient]) graph[ingredient] = []

            graph[ingredient].push(recipe)

            if (!inDegree[recipe]) inDegree[recipe]=0

            inDegree[recipe] ++
        })
    });

    let queue = [...supplies]
    let result = []
    while (queue.length) {
        let cur = queue.shift()
        for (const neighbor of graph[cur]) {
            inDegree[neighbor]--
            if (inDegree[neighbor] === 0){
                queue.push(neighbor)
                result.push(neighbor)
            }
        }
    }

    return result
}


var solution2DFS = function(recipes, ingredients, supplies){
    let graph = {}
    let canMake = {}

    for (const supply of supplies) {
        canMake[supply] = true
    }

    for (const recipe of recipes){
        graph[recipe].push(ingredients)
    }

    var DFS = (food) => {
        if (canMake.hasOwnProperty(food)) return canMake[food]
        canMake[food] = false
        if (graph.hasOwnProperty(food)){
            for (const neighbor of graph[food]){
                if (!DFS(neighbor)) return false
            }
        canMake[food] = true
        }

        return canMake[food]
    }

    let result = []
    for (const food of foods) {
        if (DFS(food)){
            result.push(food)
        }
    }

    return result
}