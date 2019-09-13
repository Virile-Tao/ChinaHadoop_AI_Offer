class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        //动态转移方程：dp[i] = max(dp[j]) + 1, 0 < j < i;
        //dp[i]表示到第i个元素有多少个最长上升子序列
        int n = nums.size();
        int curMax;
        vector<int> dp(n, 1);
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<i; j++)
            {
                if (nums[i] > nums[j]) 
                {
                    curMax = dp[j] + 1;
                    dp[i] = dp[i] > curMax ? dp[i] : curMax;
                }
            }
        }
        curMax = 0;
        for (int i=0; i<n; i++)
        {
            curMax = curMax > dp[i] ? curMax : dp[i];
        }
        return curMax;
    }
};
