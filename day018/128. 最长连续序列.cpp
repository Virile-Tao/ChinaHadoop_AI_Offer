class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> myset(nums.begin(), nums.end());
        int curLen = 0, maxLen = 0;
        for (int num : nums)
        {
            if (myset.count(num - 1) == 0)
            {
                curLen = 1;
                while (myset.count(num + 1))
                {
                    curLen++;
                    num++;
                }
                maxLen = maxLen > curLen ? maxLen : curLen;
            }
        }
        return maxLen;
    }
};
