class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 状态转移方程dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        # 时间复杂度O(MN/2)，空间复杂度O(N)
        m, n = len(triangle), len(triangle[-1])
        if m == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        print(dp)
        return min(dp[-1])
