var Solution = (strs: [string]): string[][] => {
    type hashMap = {
        [key: string]: string[]
    }
    let map = {} as hashMap;
    for (let str of strs){
        let key = str.split('').sort().join('');
        if (!map[key]){
            map[key] = [str];
        } else {
            map[key].push(str);
        }
    }

    return Object.values(map)
}
