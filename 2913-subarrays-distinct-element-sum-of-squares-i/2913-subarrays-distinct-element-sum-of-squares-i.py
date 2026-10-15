class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for i in range(len(nums)):
            sub=set()
            for j in range(i,len(nums)):
                sub.add(nums[j])
                count=len(sub)
                ans+=count**2
        return ans
                

        