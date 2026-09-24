class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            sum=0
            while nums[i]>0:
                l=nums[i]%10
                sum+=l
                nums[i]//=10
            if sum==i:
                return i
        return -1