class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int> > res;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i=0; i<n-2; i++)
        {
            while (i>0 && i<n-2 && nums[i] == nums[i-1]) i++;
            int j=i+1;
            int k=n-1;
            while (j<k)
            {
                if (nums[i] + nums[j] + nums[k] > 0) k--;
                else if (nums[i] + nums[j] + nums[k] < 0) j++;
                else 
                {
                    vector<int> tmp;
                    tmp.push_back(nums[i]);
                    tmp.push_back(nums[j]);
                    tmp.push_back(nums[k]);
                    res.push_back(tmp);
                    j++;
                    k--;
                }
                while (j>i+1 && j<k && nums[j] == nums[j-1]) j++;
                while (k<n-1 && j<k && nums[k] == nums[k+1]) k--;
            }
        }
        return res;
    }
};
