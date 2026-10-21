/**
 * @param {string} s
 * @return {boolean}
 */
var checkString = function(s) {
    t=Array.from(s).sort().join("")
    return t==s

};