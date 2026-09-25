class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        listt=[]
        for i in range(1,n+1):
            listt.append(str(i))
        listt.sort()
        ans=[]
        for i in listt:
            ans.append(int(i))
        return ans