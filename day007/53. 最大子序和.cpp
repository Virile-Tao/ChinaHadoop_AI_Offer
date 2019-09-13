class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curSum = 0;
        int maxSum = INT_MIN;
        for (int num: nums)
        {
            curSum += num;
            if (curSum < num) curSum = num;
            maxSum = maxSum > curSum ? maxSum : curSum;
        }
        return maxSum;
    }
};
