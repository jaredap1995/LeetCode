

var climbingStairs = (n) => { //Dynamic Programming
    if (n==1) return 1
    if (n ==2) return 2

    let ways = new Array(n).fill(0)
    ways[0]=1
    ways[1]=2

    for (let i =2; i<ways.length; i++){
        ways[i] = ways[i-1]+ways[i-2]
    }

    return ways[n-1]
}