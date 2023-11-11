import collections
def Solution(recipes, ingredients, supplies):
    graph = collections.defaultdict(list)
    can_make = {supply: True for supply in supplies}

    for recipe, ing in zip(recipes, ingredients):
        for i in ing:
            graph[recipe].append(i)

    def DFS(food):
        if food not in can_make:
            can_make[food]=False
            if food in graph:
                for neighbor in graph[food]:
                    if not DFS(neighbor):
                        return False
                can_make[food]=True
        
        return can_make[food]
    
    res = []
    for food in recipes:
        if DFS(food):
            res.append(food)

    return res


def Solution2_BFS(recipes, ingredients, supplies):
    graph = collections.defaultdict(list)
    # in_degree is counter for edges going in to each node
    # If in_degree reaches 0 during BFS traversal, we can make the recipe
    in_degree = collections.defaultdict(int)

    # ingredient --> recipe in topological sort approach
    for ingredient, recipe in zip(ingredients, recipes):
        for ing in ingredient:
            graph[ing].append(recipe)
            in_degree[recipe]+=1

    #BFS Traverse across all of supplies
    queue = supplies[:]
    res = []
    while queue:
        cur = queue.pop(0)
        for neighbor in graph[cur]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                res.append(neighbor)
                queue.append(neighbor)

    return res
