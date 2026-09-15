class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=[]
        for i in nums[:]:
            if i%2==0:
                temp.append(i)
                nums.remove(i)
        temp.extend(nums)
        return temp