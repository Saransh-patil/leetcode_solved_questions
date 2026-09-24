class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        for i in range(len(nums)):
            
            if i==0:
                left=0
                right=sum(list(nums[i+1:]))
                if left==right:
                    return i
            elif i==len(nums)-1:
                right=0
                left=sum(list(nums[:i]))
                if left==right:
                    return i
            else:
                left=sum(list(nums[:i]))
                right=sum(list(nums[i+1:]))
                if left==right:
                    return i
        return -1
