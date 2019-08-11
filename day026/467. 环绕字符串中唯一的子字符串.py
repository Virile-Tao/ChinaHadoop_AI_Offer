class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # 时间复杂度O(N)，空间复杂度O(1)
        # 状态转移方程dp[i] = dp[i-1] + 1
        if len(p) == 0:
            return 0
        dp = [0] * 26
        dp[ord(p[0]) - ord('a')] = 1
        last = 1
        for i in range(1, len(p)):
            if dp[ord(p[i]) - ord('a')] == 0:
                dp[ord(p[i]) - ord('a')] = 1
            j = i - 1
            if ((ord(p[i]) - ord(p[j]) + 26) % 26 == 1):
                if 1 + last > dp[ord(p[i]) - ord('a')]:
                    dp[ord(p[i]) - ord('a')] = last + 1
                last += 1
            else:
                last = 1
        ans = 0
        for i in range(26):
            ans += dp[i]
        return ans
