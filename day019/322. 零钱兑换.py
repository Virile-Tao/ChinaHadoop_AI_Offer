class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 时间复杂度O(NK)，空间复杂度O(K)
        # 动态规划dp[i] = min(dp[i], dp[i-coin])
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
    
    def coinChange_v2(self, coins: List[int], amount: int) -> int:
        # 暴力法，超时
        if amount <= 0:
            return 0
        res = float('inf')
        for coin in coins:
            if coin > amount:
                continue
            sub_prob = self.coinChange(coins, amount - coin)
            if sub_prob == -1:
                continue
            res = min(res, sub_prob + 1)
        return -1 if res == float('inf') else res
