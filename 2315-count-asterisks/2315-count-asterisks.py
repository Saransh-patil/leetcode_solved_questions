class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        count=0
        for i in s:
            if i=='|' and len(stack)==0:
                stack.append(i)
            elif i=='|' and len(stack)==1:
                stack.remove(i)
            if len(stack)>0:
                continue                
            if len(stack)==0 and i=='*':
                count+=1
        print(count)
        return count

        