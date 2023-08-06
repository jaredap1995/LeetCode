class TrieNode (object):
    def __init__ (self):
        self.children= {}
        self.isEnd = False

class Trie:
    def __init__ (self):
        self.root = TrieNode()

    def insert (self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class Solution:
    def exist(self, board, word):
        H, W = len(board), len(board[0])
        d = Trie
        d.insert(word)

        def backtrack (row_i, col_i, cur_str, cur_node):
            if cur_node.isEnd:
                return cur_str == word
            
            if row_i < 0 or col_i < 0 or row_i >= H or col_i >= W:
                return 
            
            cur_chr = board[row_i][col_i]

            if cur_chr not in cur_node.children:
                return
            
            cur_root = cur_node
            cur_node = cur_node.children[cur_chr]

            board[row_i][col_i] = "#"

            ### Recursive Loop checking every direction on board => returns boolean ####
            for dx, dy in [(-1,0), (1,0), (0-1), (0,1)]:
                if backtrack(row_i+dx, col_i+dy, cur_str+cur_chr, cur_node):
                    return True
                
            board[row_i][col_i]

            if not cur_node.children:
                del cur_root.children[cur_chr]

            return
        
        root = d.root
        for i in range(H):
            for j in range (W):
                if backtrack(i,j,"", root):
                    return True
        return False

