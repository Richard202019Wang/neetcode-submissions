class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = 0
        for i, p in enumerate(prices):
            if p < prices[buy]:
                buy = i
            else:
                
                result = max(result, p - prices[buy])

        return result
        