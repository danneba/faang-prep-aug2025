from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        if len(prices) == 1 and len(prices) == 0 and decreasingFun:
            return 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            diff = prices[i] - min_price
            if diff > max_profit:
                max_profit = diff
        return max_profit
    def decreasingFun(self, prices:List[int]) -> bool:
        for i in range(len(prices)):
            if prices[i] < prices[i+1]:
                return False
        return True

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))
