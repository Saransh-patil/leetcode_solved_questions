class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        r=0
        l=0
        s=set()
        while r<len(nums):
            if nums[r] in s:
                return True
            s.add(nums[r])
            if r-l==k:
                s.remove(nums[l])
                l+=1
            r+=1
        return False
