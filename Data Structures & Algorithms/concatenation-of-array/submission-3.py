class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # myList = []
        # for val in nums:
        #     myList.append(val)
        #     # print(myList)
        # myList.extend(nums)
        # return myList
        myList = []
        for val in range(len(nums)):
            myList.insert(val, nums[val])
            myList.insert(len(nums)+ val, nums[val])
        return myList

        # nums.extend(nums)
        # return nums