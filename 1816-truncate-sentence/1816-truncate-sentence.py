class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.split()
        res=[]
        for i in range(0,k):
            res.append(s[i])
        return " ".join(res)
