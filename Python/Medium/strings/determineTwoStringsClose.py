import collections
def solution(word1, word2):
    if len(word1) != len(word2): return False

    if set(word1) != set(word2): return False

    c1 = collections.Counter(word1)
    c2 = collections.Counter(word2)

    return sorted(list(c1.values())) == sorted(list(c2.values()))