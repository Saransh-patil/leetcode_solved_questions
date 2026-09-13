class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        ans=0
        for ch in s:
            if ch in seen:
                seen.remove(ch)
                ans+=2
            else:
                seen.add(ch)
        if len(seen)>0:
            ans+=1
        return ans
