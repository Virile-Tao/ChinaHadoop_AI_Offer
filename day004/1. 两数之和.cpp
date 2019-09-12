class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        vector<int> res;
        for (int i=0; i<nums.size(); i++)
        {
            if (m.find(nums[i]) == m.end()) m[nums[i]] = i;
            else m[nums[i]] = i;
        }
        for (int i=0; i<nums.size(); i++)
        {
            if (m.find(target-nums[i]) != m.end() && m[target - nums[i]] != i)
            {
                res.push_back(i);
                res.push_back(m[target-nums[i]]);
                return res;
            }
        }
        return res;
    }
};
