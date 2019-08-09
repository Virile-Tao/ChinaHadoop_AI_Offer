class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 状态转移方程dp[i] = prices[i] - min(prices[:i])
        # 时间复杂度O(N)，空间复杂度O(1)
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            cur_profit = prices[i] - min_price
            min_price = min(min_price, prices[i])
            max_profit = max(cur_profit, max_profit)
        return max_profit            
