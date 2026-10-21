/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    let count=0
    let word=text.split(" ");
    for (const w of word){
        let broken=false;
        for (let ch of brokenLetters){
            if (w.includes(ch)){
                broken=true
                break
            }
        }
            if (!broken){
                count++;
            }        
    }
    return count
};