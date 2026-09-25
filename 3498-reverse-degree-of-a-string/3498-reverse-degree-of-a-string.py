class Solution(object):
    def reverseDegree(self, s):
        su=0
        for i in range(len(s)):
            y=123-ord(s[i])
            su+=(i+1)*y
        return su