/**
 * @param {charachter [][]} board
 * @param {string} word
 * @return {boolean}
 */

var Trie = function (){
    this.root = {}
    this.isEnd = false
}

Trie.prototype.insert = function (word) {
    node = this.root
    for (const char of word){
        if (!node[char]){
            node[char] = {}
        }
        node = node[char]
    }
    node.isEnd = true
}

var exist = function(board, word) {
    H = board.length
    W= board[0].length

    const trie= new Trie()
    trie.insert(word)

    var backtrack = (row_i, col_i, cur_str, cur_node) => {
        if (cur_node.isEnd){
            return cur_str==word
        }

        if (row_i<0 || col_i<0 || row_i>=H || col_i >= W){
            return
        }

        cur_chr = board[row_i][col_i]

        if (!cur_node[cur_chr]){
            return
        }

        cur_root = cur_node
        cur_node = cur_node[cur_chr]

        board[row_i][col_i] = "#"

        let directions =[[-1,0], [1,0], [0,-1], [0,1]]

        for (let [dx,dy] of directions){
            if (backtrack(row_i+dx, col_i+dy, cur_str+cur_chr, cur_node)){
                return true
            }
        }
        board[row_i][col_i]

        if (!Object.keys(cur_node).length){
            delete cur_root[cur_chr]
        }

        return
    }

    root = trie.root
    for (let i = 0; i<H; i++){
        for (let j = 0; j<W; j++){
            if (backtrack(i,i,"", root)){
                return true
            }
        }
    }
    return false

}