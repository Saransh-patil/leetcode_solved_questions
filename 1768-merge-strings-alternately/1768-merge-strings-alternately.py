class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        char=""
        for i,j in zip(word1,word2):
            char+=i
            char+=j
        if len(word1)>len(word2):
            char+=word1[len(word2):]
        else:
            char+=word2[len(word1):]
        return char
