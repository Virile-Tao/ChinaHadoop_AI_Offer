class Solution:
    def rob(self, nums: List[int]) -> int:
        # 状态转移方程dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # 时间复杂度O(N)，空间复杂度O(1)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        p, q = nums[0], max(nums[0], nums[1])
        max_profit = 0
        for i in range(2, len(nums)):
            cur_profit = max(p + nums[i], q)
            max_profit = max(max_profit, cur_profit)
            p = q
            q = cur_profit
        return max_profit
