class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=list(s)
        for i in range(1,len(s),2):
            res[i]=chr(ord(s[i-1])+int(s[i]))
        return "".join(res)

            