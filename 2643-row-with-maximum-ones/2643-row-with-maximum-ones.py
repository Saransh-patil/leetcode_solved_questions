class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        index=0
        ones=0
        prev=-1
        for row in range(len(mat)):
            c=mat[row].count(1)
            if c>prev:
                index=row
                ones=c
                prev=c
        return [index,ones]
