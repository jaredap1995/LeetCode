var solution = function(right, left){
    while (right > left) {
        right = right & (right - 1)
    }
    return right & left
}
