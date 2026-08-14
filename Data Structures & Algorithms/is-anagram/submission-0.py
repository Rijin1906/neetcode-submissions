class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict1 = {}
        myDict2 = {}
        if (len(s) == len(t)):
            # loop for s string
            for val in range(len(s)):
                char = s[val]
                if char not in myDict1:
                    myDict1[char] = 1
                else:
                    myDict1[char] += 1

            # loop for t string
            for val in range(len(t)):
                char = t[val]
                if char not in myDict2:
                    myDict2[char] = 1
                else:
                    myDict2[char] += 1
            if myDict1 == myDict2:
                return True
            else:
                return False
        else:
            return False