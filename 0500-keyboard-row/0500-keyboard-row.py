class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"
        result=[]
        for w in words:
            count1,count2,count3=0,0,0
            x=w
            w=w.lower()
            for i in w:
                if i in first_row:
                    count1+=1
                elif i in second_row:
                    count2+=1
                elif i in third_row:
                    count3+=1
            if count1==len(w) or count2==len(w) or count3==len(w):
                result.append(x)
        return result