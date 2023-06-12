
//You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the 
//i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

//A customer's wealth is the amount of money they have in all their bank accounts. 
//The richest customer is the customer that has the maximum wealth.


/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    var sums=[];
    for (let account of accounts) {
        var sum = account.reduce ((a,b) =>
            a+b);
        sums.push(sum);}
return Math.max(...sums)
};