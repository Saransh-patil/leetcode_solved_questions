class Solution:
    def greatestLetter(self, s: str) -> str:
        a=s.lower()
        res=""
        for i in a:
            if i.upper() in s and i.lower() in s:
                res+=i.upper()
        m=list(res)
        if m:
            return max(m)
        else:
            return res