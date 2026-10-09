class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        for i in range(1,len(s)):
            x=s[i]
            y=s[i-1]
            total+=(abs(ord(x)-ord(y)))
        return total

        