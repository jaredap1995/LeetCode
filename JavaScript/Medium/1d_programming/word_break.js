var wordBreak = function (s, word_dict){
    let n=s.length
    let dp = new Array(n+1).fill(false)
    dp[0] = true

    for (let i = 1; i<n+1; i++) {
        for (word of word_dict) {
            if (i-word.length >= 0 && dp[i-word.length] && s.slice(i-word.length, i) == word) {
                dp[i]= true
                break
            }
        }
    }

    return dp[n]
}