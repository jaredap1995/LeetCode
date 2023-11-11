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