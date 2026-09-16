class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min=float('inf')
        nums.sort()
        for i in range(len(nums)-k+1):
            diff=nums[i+k-1]-nums[i]
            if diff<min:
                min=diff
        return min


        