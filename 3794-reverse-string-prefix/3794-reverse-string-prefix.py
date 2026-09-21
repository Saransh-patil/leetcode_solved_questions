class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=list(s)
        s[0:k]=s[0:k][::-1]
        return "".join(s)