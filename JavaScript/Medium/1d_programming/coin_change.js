/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

const char = 1;

var coinChnage = function (coins, amount) {
    if (amount == 0){ return 0}
    coins = coins.sort((a,b)=>b-a)

    let minCount = new Array(coins.length+1).fill(Infinity)
    minCount[0]=0

    for (let num = 1; num<=amount; num++){
        for (let coin of coins){
            if (coin > num) { break }

            minCount[num] = Math.min(minCount[num], char+minCount[num-coin])
        }
    }
}

coins = [3,1,5]
amount=3
coinChnage(coins, amount)