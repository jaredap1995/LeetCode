class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = {}

class Trie:
    def __init__(self, total_words):
        self.root = TrieNode()
        self.unfound_words = total_words

    def insert (self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class Solution(object):
    def findWords(self, board, words):
        result = []
        H, W = len(board), len(board[0])
        d = Trie(len(words)) #Pass how many words exist in Trie

        for word in words:
            d.insert(word) #Insert each word into Trie

        def go(row_index, col_index, current_word, current_node):
            if current_node.isEnd: #base case
                result.append(current_word) #If current node is end of word, append and substract unfound words.
                current_node.isEnd = False
                d.unfound_words = -1

            if d.unfound_words == 0: #If no words in board then return
                return
            
            if row_index < 0 or col_index < 0 or row_index >= H or col_index >= W:
                return #If out of bounds, return
            
            current_charachter = board[row_index][col_index] #Set current charachter starting at board[0][0] and saves it

            if current_charachter not in current_node.children:
                return #Check if the charachter is a child of current node, for the root node it will always be True, but later cases it wont be
                        # This will check for if we are actually scanning in the direction of a word on the board
            
            current_root = current_node #Previous condition passes, current charachter is in previous node children, set current root
            current_node = current_node.children[current_charachter] #Pass from current root to next valid node that continues a word]

            board[row_index][col_index] = '59' #Marking this cell to ensure that on recursive calls we do not end up in infinite loop

            go(row_index+1, col_index, current_word+current_charachter, current_node)
            go(row_index-1, col_index, current_word+current_charachter, current_node)
            go(row_index, col_index+1, current_word+current_charachter, current_node)
            go(row_index, col_index-1, current_word+current_charachter, current_node)

            board[row_index][col_index] = current_charachter

            if not current_node.children: #Delete any nodes that don't have vhildren to skrink size of the Trie
                del current_root.children[current_charachter]
            
            return
        
        root = d.root
        for i in range(W):
            for j in range(H):
                if d.unfound_words == 0:
                    return result
                go(i,j,"", root)

        return result



            


