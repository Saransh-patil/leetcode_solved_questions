class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=""
        res=[]
        for i in nums:
            s+=str(i)
        for i in s:
            res.append(int(i))
        return res
