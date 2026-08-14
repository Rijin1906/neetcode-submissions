class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dict = {}
        # count = 1
        # for val in nums:
        #     if val not in dict:
        #         dict[val] = count
        #     elif val in dict:
        #         # newVal = dict[val]
        #         dict[val] = count+1
        # for key in  dict:
        #     if(dict[key]>1):
        #         return True
        # return False

        if len(nums) == len(set(nums)):
            return False
        else:
            return True