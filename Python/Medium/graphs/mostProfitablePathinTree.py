import collections
class Solution:
    def mostProfitablePath(self, edges, bob: int, amount) -> int:

        graph = collections.defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        # depth of bob traversal path (DFS)
        self.bob_path = []
        def dfs(node, parent, path):
            if node == 0:
                self.bob_path = list(path)
                return True
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                path.append(neighbor)
                if dfs(neighbor, node, path):
                    return True
                path.pop()
            
            return False
        
        dfs(bob, -1, [bob])
        step = dict()
        for i in range(len(self.bob_path)):
            step[self.bob_path[i]] = i

        # loop all possible Alice traversal path (BFS)
        ans = float('-Inf')
        # Base case if bob is also at node 0
        profit_ini = amount[0] if bob != 0 else amount[0] // 2


        que = collections.deque([(0, -1, profit_ini)])
        depth = 0
        while que:
            for _ in range(len(que)):
                cur, parent, profit = que.pop(0)
                
                if cur != 0 and len(graph[cur]) == 1:
                    ans = max(ans, profit)
                
                for neighbor in graph[cur]:
                    if neighbor == parent:
                        continue      
                    # case where either alice node was not encountered by bob or it is in bob's path but he is not yet there
                    if neighbor not in step or depth + 1 < step[neighbor]:
                        new_profit = amount[neighbor]
                    # Reached at same time (depth of neighbor == the depth of bob (as indicated by i in step))
                    elif depth + 1 == step[neighbor]:
                        new_profit = amount[neighbor] // 2
                    else:
                        new_profit = 0
                    que.append((neighbor, cur, profit + new_profit))

            depth += 1

        return ans