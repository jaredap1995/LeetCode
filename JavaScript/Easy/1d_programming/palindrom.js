var isPalindrome = function(s) {
    var valid = (s) => {
        return /^[a-zA-Z0-9]+$/.test(s);
    }

    let i = 0
    let j = s.length-1

    while (i<j) {
        while (i<j && !valid(s[i])){i++
        } 
        while (i<j && !valid(s[j])){
            j--
        }  
        if (s[i].toLowerCase()!=s[j].toLowerCase()) { return false }
        i++
        j--
    }
    return true
};