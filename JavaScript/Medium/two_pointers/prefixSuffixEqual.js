var solution = function(s){
    let right = s.length -1
    let left = 0

    while (left < right && s.charAt(left) === s.charAt(right)){
        let char = s.charAt(left)
        while (left <= right && s.charAt(left) == char){
            left ++
        }
        while (left <= right && s.charAt(right) == char){
            right --
        }
    }

    return 0 ? left > right : right - left + 1
}