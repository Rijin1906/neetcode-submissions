class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for val in range(len(nums)):
            for i in range(val+1, len(nums)):
                if(nums[val] + nums[i] == target):
                    return [val, i]
        