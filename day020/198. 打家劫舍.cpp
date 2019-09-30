class Solution {
public:
    int rob(vector<int>& nums) {
        int preMax = 0, curMax = 0;
        for (int num : nums)
        {
            int tmp = curMax;
            curMax = preMax + num > curMax ? preMax + num : curMax;
            preMax = tmp;
        }
        return curMax;
    }
};
