class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myDict = {}
        for val in range(len(nums)):
            myValue = nums[val]
            if myValue in myDict:
                myDict[myValue] += 1
            else:
                myDict[myValue] = 1
        
        maxValue = 0
        maxKey = 0
        for key in myDict:
            if myDict[key]> maxValue:
                maxKey = key
                maxValue = myDict[key]
        return maxKey  