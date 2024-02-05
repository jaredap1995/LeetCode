var solution = function(s, t) {
    if (s === t) return t
    let left = 0; let right = 0;
    let start = 0; let end = 0;

    var Counter = (arr) => {
        let dict = {}
        for (let i = 0; i<arr.length; i++){
            dict[arr[i]] = (dict[arr[i]] || 0) + 1
        }

        return dict
    }

    let countT = Counter(t)
    let window = {}
    let need = t.length

    let windowSize = Infinity

    while (right < s.length){
        window[s[right]] = (window[s[right]] || 0) + 1
        if (t.includes(s[right])){
            if (window[s[right]] <= countT[s[right]]){
                need --
            }
        }
        right ++

        while (need === 0){
            if (right - left < windowSize){
                end = right
                start = left
                windowSize = right - left
            }
            if (t.includes(s[left])){
                window[s[left]] --
                if (window[s[left]] < countT[s[left]]){
                    need ++
                }
            }
        left ++
        }
    }

    if (windowSize === Infinity) return ""
    else return s.slice(start, end)
}