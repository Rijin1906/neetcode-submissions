class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        myList = []
        myDict = {}

        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]] = 1
            else:
                myDict[nums[i]] += 1
        
        for i in range(len(nums)):
            if i+1 not in myDict:
                myList.append(i+1)
        
        return myList