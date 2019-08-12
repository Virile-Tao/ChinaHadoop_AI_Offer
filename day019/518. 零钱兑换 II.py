class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 时间复杂度O(NK)，空间复杂度O(K)
        # 动态规划，dp[i+coin] += dp[i]
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]
