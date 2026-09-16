class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minus=0
        plus=0
        for i in nums:
            if i<0:
                minus+=1
            elif i>0:
                plus+=1
        return max(minus,plus)
