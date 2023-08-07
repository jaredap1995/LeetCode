/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length ===0) {return []}

    const keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
    let result = []

    var backtrack = (combination, next_digits) => {
        if (next_digits.length === 0){
            result.push(combination)
        }
        else {
            const letters = keyboard[next_digits[0]]
            for (let letter of letters){
                backtrack(combination + letter, next_digits.slice(1));
            }
        }
            
        }
        backtrack("", digits)
        console.log(result)
    }

letterCombinations("23")