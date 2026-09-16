class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        temp=sorted(s)
        temp2=sorted(t)
        res=[]
        for i in temp2:
            if i in temp:
                temp.remove(i)
            else:
                res.append(i)
                    
        return "".join(res)