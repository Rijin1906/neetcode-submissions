class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myDict = {}

        for i in range(len(nums)):
            myDict[nums[i]] = 1
            
        
        nums.clear()

        for i in myDict:
            nums.append(i)
        
        # nums.sort()

        return len(nums)