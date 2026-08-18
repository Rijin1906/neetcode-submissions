class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        flag = False
        index = -1
        
        for i in range(len(nums)):
            sum += nums[i]

        for j in range(len(nums)):
            left = 0
            right = 0

            #left addition
            for k in range(0, j):
                left += nums[k]
            
            #right addition
            for l in range(j+1, len(nums)):
                right += nums[l]
            
            if left == right:
                index = j
                flag = True
                break
        
        if flag == True:
            return index
        else:
            return index

            


