class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // one-hot code
        int n = nums.size();
        int len = 1 << n;
        vector<vector<int> > res;
        for (int i=0; i<len; i++)
        {
            vector<int> tmp;
            for (int j=0; j<n; j++)
                if (i & 1<<j) tmp.push_back(nums[j]);
            res.push_back(tmp);    
        }
        return res;
    }
};
