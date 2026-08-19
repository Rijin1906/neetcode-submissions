class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        count = 0
        localCount = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                localCount+= 1
                if localCount >= count:
                    count = localCount
        
            if nums[i] == 0:
                localCount = 0
            
        return count