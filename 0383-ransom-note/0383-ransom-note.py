class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r1=sorted(ransomNote)
        r2=sorted(magazine)
        for i in r1[:]:
            if i in r2:
                r1.remove(i)
                r2.remove(i)
        print(r1)
        if len(r1)==0:
            return True
        return False