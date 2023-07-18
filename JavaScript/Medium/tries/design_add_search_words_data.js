function TrieNode (children, isEnd){
    this.children = new Object()
    this.isEnd = false
}

var WordDictionary = function (){
    this.root = new TrieNode()
}

WordDictionary.prototype.insert = function(word){
    node = this.root
    for (char of word){
        if (!node.children[char]){
            node.children[char] = new TrieNode()
        }
        node = node.children[char]
    }
    node.isEnd = true;
}

WordDictionary.prototype.search = function (word){
    var dfs = function(node, nodeIndex){
        if (nodeIndex == word.length) {
            return node.isEnd
        }

        if (word[nodeIndex] == '.'){
            for (var child in node.children){
                if (dfs(node.children[child], nodeIndex+1)){
                    return true
                }
            }
        } else if (node.children[word[nodeIndex]]) {
            return dfs(node.children[word[nodeIndex]], nodeIndex+1);
        }
        return false
    }
    return dfs(this.root, 0)
};