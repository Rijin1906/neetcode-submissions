class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            myStr = details[i]
            a = myStr[11]
            b = myStr[12]
            if int(a+b) >60:
                count+= 1
        
        return count
