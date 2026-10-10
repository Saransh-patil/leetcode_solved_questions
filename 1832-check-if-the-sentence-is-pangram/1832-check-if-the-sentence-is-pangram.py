class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s="abcdefghijklmnopqrstuvwxyz"
        for i in sentence:
            if i in s:
                s=s.replace(i,"")
        return len(s)==0