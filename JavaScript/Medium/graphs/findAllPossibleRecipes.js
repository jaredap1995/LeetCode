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