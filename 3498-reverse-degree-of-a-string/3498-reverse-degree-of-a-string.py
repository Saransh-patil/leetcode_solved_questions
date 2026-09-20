class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary={}
        y=90
        x=122
        for i in range(1,27):
            m=str(chr(x))
            n=str(chr(y))
            dictionary[m]=i
            dictionary[n]=i
            y-=1
            x-=1
        sum=0
        for i in range(len(s)):
            if s[i] in dictionary:
                sum+=dictionary[s[i]]*(i+1)
        return sum

        