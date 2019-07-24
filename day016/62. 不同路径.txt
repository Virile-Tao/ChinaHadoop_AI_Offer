class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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
