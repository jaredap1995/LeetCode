var quickSort = (arr) => {
    if (arr.length <= 1) {
        return arr
    }

    let mid = arr[Math.floor(arr.length/2)]
    let left = []
    let right = []
    let middle = []

    for (x of arr) {
        if (x<mid) {
            left.push(x)
        }
        else if (x > mid) {
            right.push(x)
        }
        else{
            middle.push(x)
        }
    }

    return quickSort(left).concat(middle, quickSort(right))
}

arr = [6,10,1,100,27,9]
console.log(quickSort(arr))