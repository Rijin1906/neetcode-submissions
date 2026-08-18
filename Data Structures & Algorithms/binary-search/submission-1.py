class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idxCount = -1
        for i in range(len(nums)):
            if target == nums[i]:
                idxCount = i
                break
        return idxCount
                
