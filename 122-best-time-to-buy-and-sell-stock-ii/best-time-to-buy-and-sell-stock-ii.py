class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value = []

        for num in range(1,len(prices)):
            if prices[num-1] < prices[num]:
                value.append(prices[num]-prices[num-1])
            
        return sum(value)