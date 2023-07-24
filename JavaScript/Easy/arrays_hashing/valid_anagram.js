/**
 * 
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */


var isAnagram = function (s,t){
    const ns = s.split('').sort().toString();
    const nt = t.split('').sort().toString();
    return ns == nt;
}