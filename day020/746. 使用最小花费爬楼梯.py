class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 状态转移方程：dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        # 时间复杂度O(N)，空间复杂度O(1)
        pre2_cost, pre1_cost = cost[0], cost[1]
        cur_cost = min(cost[0], cost[1])
        for i in range(2, len(cost)):
            cur_cost = min(pre2_cost, pre1_cost) + cost[i]
            pre2_cost = pre1_cost
            pre1_cost = cur_cost
        return min(pre2_cost, cur_cost)
