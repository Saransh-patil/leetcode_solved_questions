class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max=0
        for i in range(len(accounts)):
            temp=0
            for j in range(len(accounts[i])):
                temp+=accounts[i][j]
            if temp>max:
                max=temp
        return max


