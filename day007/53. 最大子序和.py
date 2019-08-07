class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(1)
        # 动态规划，当前子序列的和大于0，则继续向后累加计算，
        # 如果当前子序列和小于等于0，则说明前面子序列和起负作用，舍去重新开始一个子序列计算
        res, sub_sum = nums[0], 0
        for num in nums:
            if sub_sum > 0:
                sub_sum += num
            else:
                sub_sum = num
            res = max(res, sub_sum)
        return res
