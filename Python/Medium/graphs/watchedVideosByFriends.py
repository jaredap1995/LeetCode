import collections
from itertools import chain
def solution(watchedVideos, friends, id, level):
    graph = collections.defaultdict(list)
    for idx,friend in enumerate(friends):
        graph[idx].extend(friend)

    # cur_node, level
    queue = [(id, 0)]
    visited = set([id])
    friends_at_level = set()

    while queue:
        cur_node, cur_level = queue.pop(0)
        if cur_level == level:
            friends_at_level.add(cur_node)
        elif cur_level < level:
            for neighbir in graph[cur_node]:
                if neighbir not in visited:
                    visited.add(neighbir)
                    queue.append((neighbir, cur_level + 1))

    
    vidoes_counter = collections.Counter(chain.from_iterable([watchedVideos[friend] for friend in friends_at_level]))

    return sorted(vidoes_counter.keys(), key = lambda x: (vidoes_counter[x], x))