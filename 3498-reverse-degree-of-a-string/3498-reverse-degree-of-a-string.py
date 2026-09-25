class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)) :
            sum += (i+1) * (26 - (ord(s[i])-ord('a')))
        return sum
        