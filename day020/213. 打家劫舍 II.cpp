class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        int preMax = 0, curMax = 0, tmp;
        for (int i=0; i<n-1; i++)
        {
            tmp = curMax;
            curMax = preMax + nums[i] > curMax ? preMax + nums[i] : curMax;
            preMax = tmp;
        }
        int first = curMax;
        preMax = 0; curMax = 0;
        for (int i=1; i<n; i++)
        {
            tmp = curMax;
            curMax = preMax + nums[i] > curMax ? preMax + nums[i] : curMax;
            preMax = tmp;
        }
        return first > curMax ? first : curMax;
    }
};
