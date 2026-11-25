class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        res=sorted(nums)
        return res[-k]