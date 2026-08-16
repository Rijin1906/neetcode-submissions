class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse = s[ : : -1]
        for i in range(len(reverse)):
           s[i] = reverse[i]
        
        