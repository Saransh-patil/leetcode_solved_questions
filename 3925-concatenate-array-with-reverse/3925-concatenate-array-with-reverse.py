class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=reversed(nums)
        nums.extend(x)
        return nums