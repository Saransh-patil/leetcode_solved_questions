class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        dictionary={}
        for row in knowledge:
            dictionary[row[0]]=row[1]
        print(dictionary)
        res=""
        i=0
        while i<len(s):

            if s[i]=="(":
                j=i+1
                while s[j]!=')':
                    j+=1
                key=s[i+1:j]

                if key in dictionary:
                    res+=dictionary[key]
                else:
                    res+='?'
                i=j+1
            else:
                res+=s[i]
                i+=1
        return res
            
            