var solution = function(tokens){
    var arithmetic = (operator, num1, num2) => {
        num1 = parseInt(num1)
        num2 = parseInt(num2)

        if (operator === '+') return num1 + num2
        else if (operator === '-') return num1 - num2
        else if (operator === '*') return num1 * num2
        else return Math.trunc(num1 / num2)
    }

    let stack = []
    let ops = ['+', '-', '*', '/']
    for (let token of tokens){
        if (!ops.includes(token)){
            stack.push(token)
        } else {
            let num2 = stack.pop()
            let num1 = stack.pop()

            stack.push(arithmetic(token, num1, num2))
        }
    }

    return stack[0]
}