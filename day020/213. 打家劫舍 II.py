class Solution:
    def rob(self, nums: List[int]) -> int:
        # 状态转移方程dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # 时间复杂度O(N)，空间复杂度O(1)
        # 由于不能同时抢第一间和最后一间，故去掉第一间抢和去掉第二间抢，返回最大值
        if not nums:
                return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def rob_base(nums):
            if len(nums) == 2:
                return max(nums[0], nums[1])
            p, q = nums[0], max(nums[0], nums[1])
            max_p = 0
            for i in range(2, len(nums)):
                cur_p = max(p + nums[i], q)
                p, q = q, cur_p
                max_p = max(max_p, cur_p)
            return max_p
                
            
        return max(rob_base(nums[:len(nums) - 1]), rob_base(nums[1:]))
