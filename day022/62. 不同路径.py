class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划，时间复杂度O(mn), 空间复杂度O(mn)
        # dp[i][0] = 1, dp[0][j] = 1
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
    
    def uniquePaths_v2(self, m: int, n: int) -> int:
        # 时间复杂度O(n+m)，空间复杂度O(1)
        # 排列组合，左上角到右下角共要走(n-1)+(m-1)步，其中向下走(n-1)步，向右(m-1)步
        # 题目变为，总共走(n+m-2)步，其中有(n-1)步向下走，共有多少种走法。
        # 则由排列组合算法：(n+m-2)!/((n-1)!*(m-1)!)
        fenzi, fenmu1, fenmu2 = 1, 1, 1
        for i in range(2, m+n-1):
            fenzi *= i
        for i in range(2, n):
            fenmu1 *= i
        for i in range(2, m):
            fenmu2 *= i
        return fenzi//(fenmu1*fenmu2)
