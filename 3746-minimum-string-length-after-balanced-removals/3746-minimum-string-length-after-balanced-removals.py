class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=""
        x=s.count('a')
        y=s.count('b')
        if x>y:
            temp=x-y
            for i in range(temp):
                res+='a'
            return len(res)
        elif y>x:
            temp=y-x
            for i in range(temp):
                res+='b'
            return len(res)
        else:
            return 0