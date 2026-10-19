/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    x=0
    for (const i of sentences){
    if (i.split(" ").length>x){
        x=i.split(" ").length
    }
    }
    return x
};