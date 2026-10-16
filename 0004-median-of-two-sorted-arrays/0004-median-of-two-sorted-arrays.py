class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        s=sorted(nums1+nums2)
        if len(s)%2==0:
            return (s[(len(s)//2)-1]+s[(len(s)//2)])/2  
        else:
            return s[len(s)//2]
        