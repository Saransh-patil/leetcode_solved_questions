/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    let count=0
    for (const i of patterns){
        if (word.includes(i)){
            count++;
        }    
    }
    return count
};