class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        myList = []
        for val in nums:
            myList.append(val)
            # print(myList)
        myList.extend(nums)
        return myList


        # nums.extend(nums)
        # return nums