class Solution:
    def climbStairs(self, n: int) -> int:
        # 时间复杂度(N)，空间复杂度O(1)
        # 斐波那切数列，f(n) = f(n-1) + f(n-2)
        if n == 1:
            return 1
        i, j = 1, 2
        for _ in range(2, n):
            i, j = j, i + j
        return j
            
