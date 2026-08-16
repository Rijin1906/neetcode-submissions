class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse = s[ : : -1]
        rev = []
        for i in range(len(s)-1,-1,-1):
            rev += s[i] 
        for i in range(len(rev)):
           s[i] = rev[i]
        