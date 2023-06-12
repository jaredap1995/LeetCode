/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let start =0;
    let end=1;
    let max_profit=0;
    while (end<prices.length){
        if (prices[start]<prices[end]){
            let profit=prices[end]-prices[start];
            max_profit=Math.max(profit, max_profit);
        } else {
            start=end
        };
        end++
    };
    return max_profit
};