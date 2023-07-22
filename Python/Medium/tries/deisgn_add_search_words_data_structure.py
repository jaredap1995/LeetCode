class TrieNode (object):
    def __init__(self, children, isEnd):
        self.children = {}
        self.isEnd = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word):
        def dfs(node, node_index):
            if node_index == len(word):
                return node.isEnd
            
            if word[node_index] == '.':
                for char in node.children:
                    if dfs(node.children[char], node_index+1):
                        return True
            
            elif word[node_index] in node.children:
                return dfs(node.children[word[node_index]], node_index+1)
            
            return False
        return dfs(self.root, 0)