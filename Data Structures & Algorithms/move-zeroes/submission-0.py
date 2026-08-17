class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        newList = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                newList.append(nums[i])
        
        for j in range(count):
            newList.append(0)
        
        nums.clear()

        for k in range(len(newList)):
            nums.append(newList[k])

        