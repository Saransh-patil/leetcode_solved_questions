class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=""
        for i in s:
            if i=="i":
                output=output[::-1]
            else:
                output+=i
        return output