class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m=[]
        n=[]
        for i in nums:
            if i%2==0:
                m.append(i)
            else:
                n.append(i)
        return m+n