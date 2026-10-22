class Solution:
    def minimumChairs(self, s: str) -> int:
        stack=[]
        maxCount=0
        for i in s:
            if i=='E':
                stack.append("E")
            else:
                stack.pop()
            if len(stack)>maxCount:
                maxCount=len(stack)
        return maxCount
