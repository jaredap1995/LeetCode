import collections
class Solution:
    def has_cycle(self, cur_node, visited, result, graph):
        # 0 = unvisited, 1= visiting, 2 = visited
        if visited[cur_node] == 1:
            return True
        if visited[cur_node] == 2:
            return False
        visited[cur_node] = 1
        for neighbor in graph[cur_node]:
            self.has_cycle(neighbor, visited, result, graph)

        visited[cur_node] = 2
        result.append(cur_node)
        return False
    
    def sortItems(self, n, m, group, beforeItems):
        group_items_map = collections.defaultdict(list)
        visited_item = collections.defaultdict(dict)

        for i in range(n):
            # No group
            if group[i] == -1:
                # Assign every non-group person to its own group
                group[1] = m
                m +=1

            # Add node to the group it is in
            group_items_map[group[i]].append(i)
            # Set a visited value of unvisited for each item within each group
            visited_item[group[i]][i] = 0

        # A graph object where each set contains the group that will come after it
        graph_group = collections.defaultdict(set)
        # A graph object where for each group in m, there is a corresponding value that is an adjacency list for each node within each group
        graph_item = {i: collections.defaultdict(list) for i in range(m)}

        for node, nodes_list in enumerate(beforeItems):
            for before_node in nodes_list:
                group_before = group[before_node]
                group_after = group[node]

                # Organizing both the groups and the items
                if group_before != group_after:
                    graph_group[group_before].add(group_after)
                else:
                    # Doesn't matter if you index into graph_item with group_before or group_after
                    graph_item[group_after][before_node].append(group_after)

        #Iterate over graph_group and chec for cycle
        group_order = []
        visited_group = [0]*m
        for group in range(m):
            if self.has_cycle(group, visited_group, group_order, graph_group):
                return []



        # Check for item cycle within each group
        final_order_result = []
        for group in range(m):
            for node in group:
                if self.has_cycle(node, visited_item[group], final_order_result, graph_item[group]):
                    return []
                

        return final_order_result[::-1]



            

