class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        myList = heights.copy()
        myList.sort()
        count = 0

        for i in range(len(heights)):
            if myList[i] != heights[i]:
                count+=1
        return count