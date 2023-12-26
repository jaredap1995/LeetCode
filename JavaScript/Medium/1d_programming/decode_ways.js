var numDecodings = function(s) {
    // charachter code 65-90 are A-Z
    const chars = {}
    for (let i = 65; i<=90; i++){
        chars[i-64]=String.fromCharCode(i)
    }
    //Initiate array with zeros and make dp[0]=1
    let dp = new Array(s.length+1).fill(0)
    dp[0]=1

    for (let i = 1; i<=s.length; i++){
        for (let j = 0; j<=i-1; j++){
            let sub = s.substring(j,i)

            if (sub in chars) {
                dp[i]+=dp[j]
            }
        }
    }
    console.log(dp)
    console.log(dp.at(-1))
    return dp.at(-1)

}
s='1104'
numDecodings(s)


var solution2 = function(s){
    let decoder = new Set()
    for (let i = 1; i< 27; i++){
        decoder.add(i.toString())
    }

    let memo = {}

    var dfs = (i) => {
        if (i === s.length) return 1
        if (s[i] === '0') return 0
        if (memo[i] !== undefined) return memo[i]

        let res = dfs(i+1)

        if (i + 1 < s.length && decoder.has(s.substring(i, i+2))){
            res = dfs(i+2)
        }

        memo[i] = res
        return res
    }

    return dfs(0)
}




const numDecodings2 = (s) => {
	

    const decoder = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z",
    };

    // s[0] will be 1 to start off the dynamic process
    let dp = new Array(s.length + 1).fill(0);
    dp[0] = 1; // [1, 0, 0, ...., 0]

    // We want to know how many combinations we have up to a certain point
    // This will involve a double for loop where we will only go
    // up to iterater i, then next iteration push iteration i
    // and continue to search

    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j <= i - 1; j++) {
            let sub = s.substring(j, i);

            if (sub in decoder) {
                dp[i] += dp[j];
            }
        }
    }

    return dp.at(-1); // similar to in python you can do dp[-1]
};



