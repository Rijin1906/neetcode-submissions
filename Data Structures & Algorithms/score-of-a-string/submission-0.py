class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        
        for i in range(1, len(s)):
            positiveVal = ord(s[i]) - ord(s[i-1])
            if positiveVal < 0:
                positiveVal *= -1
            sum+= positiveVal
        return sum
            