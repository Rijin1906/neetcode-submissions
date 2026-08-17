class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str2 =""
        for i in range(len(s)):
            if s[i].isalnum():
                str2+= s[i]
        if str2.lower() == str2.lower()[: : -1]:
            return True
        else:
            return False