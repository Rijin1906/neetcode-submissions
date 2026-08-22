class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                sum = 0

                if prices[i] < prices[j]:
                    sum = prices[j] - prices[i]
                
                if sum > maximum:
                    maximum = sum
        
        return maximum