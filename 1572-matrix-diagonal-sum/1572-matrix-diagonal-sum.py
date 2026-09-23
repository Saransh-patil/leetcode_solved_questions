class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if len(mat)==1:
            return mat[0][0]
        
        sum=0
        n=len(mat)-1
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row==col:
                    sum+=mat[row][col]
                elif row+col==n:
                    sum+=mat[row][col]
        return sum