class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # 时间复杂度O(KN^2)，空间复杂度O(NK)
        # 状态转移方程dp[i][k] = max(dp[i][k], dp[j][k - 1] + 1.0 * (total[i] - total[j]) / (i - j))
        n = len(A)
        dp = [ [0] * (K+1) for _ in range(n+1)]
        total = [0] * (n+1)
        
        for i in range(1, n+1):
            total[i] = total[i-1] + A[i-1]
            dp[i][1] = total[i] / i
            
        for i in range(1, n+1):
            for k in range(2, K+1):
                for j in range(i):
                    dp[i][k] = max(dp[i][k], dp[j][k-1] + (total[i]-total[j]) / (i-j))
        
        # print(dp)
        return dp[n][K]
        
