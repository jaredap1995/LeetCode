var mergeSort = function(arr) {
    if (arr.length <=1) {
        return arr
    }

    let merged = []
    let mid = Math.floor(arr.length/2)
    console.log(mid)
    let left = mergeSort(arr.slice(0,mid))
    console.log(left)
    let right = mergeSort(arr.slice(mid))
    console.log(right)

    i=j=0

    while (i < left.length && j <right.length) {
        if (left[i] < right[j]) {
            merged.push(left[i])
            i++
        } else {
            merged.push(right[j])
            j++
        }
    }

    while (i < left.length) {
        merged.push(left[i])
        i++
    }

    while (j<right.length) {
        merged.push(right[j])
        j++
    }

    return merged
}

arr = [6,10,1,100,27,9]
console.log(mergeSort(arr))