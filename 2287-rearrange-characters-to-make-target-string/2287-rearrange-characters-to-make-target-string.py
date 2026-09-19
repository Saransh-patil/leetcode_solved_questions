class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        dictionary={}
        listt=[]
        for i in s:
            dictionary[i]=dictionary.get(i,0)+1
        for i in target:
            listt.append(dictionary.get(i,0)//target.count(i))
        return min(listt)



        