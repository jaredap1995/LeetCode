/**
 * @param {string} s 
 * The values in the string that represent the longest palindrome can be
 * represented by a table 'dp'
 * That table where dp[2][3]=s[2:3]
 */

var longestPalindrome = function(s) {
    let longest = '';
    const dp_table = Array.from({ length: s.length } , () => Array(s.length).fill(0))
    for (let i = 0; i<s.length; i++){
        dp_table[i][i]=true;
        longest=s.charAt(i)
    }

    for (let i = s.length-1; i>=-1; i--) {
        for (let j = i+1; j<s.length; j++){
            if (s.charAt(i) == s.charAt(j)) {
                if (j-i == 1 == true || dp_table[i+1][j-1] == true) {
                    dp_table[i][j]=true
                    if (longest.length < s.slice(i, j+1).length) {
                        longest = s.slice(i, j+1)
                    }
                }

            }
        }
    }

    console.log(longest)
    return longest


}

s = ""
longestPalindrome(s)