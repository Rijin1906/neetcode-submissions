class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        if len(nums)>=4:
            nums.sort()
            prod =( nums[-1] * nums[-2]) - (nums[0]*nums[1])
        return prod

