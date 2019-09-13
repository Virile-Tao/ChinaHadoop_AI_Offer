class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        map<int,int> m;
        for (int num: nums)
        {
            if (m.find(num) == m.end()) m[num] = 1;
            else m[num]++;
            if (m[num] > n/2) return num;
        }
        return -1;
    }
    
    int majorityElement_v2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size()/2];
    }
};
