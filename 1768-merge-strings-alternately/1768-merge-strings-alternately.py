class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        listt=[]
        t=(word1)
        t2=(word2)
        if len(t)>len(t2):
            temp=t
        else:
            temp=t2
        for i in range(len(temp)):
            if len(t)>i:
                listt.append(t[i])
            if len(t2)>i:
                listt.append(t2[i])
        return "".join(listt)

