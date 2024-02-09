import collections
def solution(strs):
    hash_map = collections.defaultdict(lambda: [])
    for word in strs:
        hash_map[''.join(sorted(word))].append(word)

    return hash_map.values()
