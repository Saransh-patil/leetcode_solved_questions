class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s=list(set(arr))
        max=-1
        for i in s:
            if arr.count(i)>max:
                if arr.count(i)==i:
                    max=arr.count(i)
        return max
