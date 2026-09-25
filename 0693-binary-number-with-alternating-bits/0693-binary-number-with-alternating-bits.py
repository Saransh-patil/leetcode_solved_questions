class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=bin(n)[2:]
        for i in range(len(t)-1):
            if t[i+1]==t[i]:
                return False
        return True