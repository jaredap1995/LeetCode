


function TrieNode (children, isEnd) {
    this.children = new Object()
    this.isEnd = false
}

var Trie = function(){
    this.root = new TrieNode()
}

Trie.prototype.insert = function (word){
    node = this.root
    for (char in word) {
        if (!node.children[char]) {
            node.children[char] = new TrieNode()
        }
        node = node.children[char]
    }
    node.isEnd = true
}

Trie.prototype.search = function(word){
    node = this.root
    for (char in word) {
        if (!node.children[char]){
            return false
        }
        node = node.children[char]
    }
    return node.isEnd
}

Trie.prototype.startsWith = function(prefix){
    node = this.root
    for (char in prefix){
        if (!node.children[char]){
            return false
        }
        node = node.children[char]
    }
    return false
}
