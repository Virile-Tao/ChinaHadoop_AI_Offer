class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0;
        int high = nums.size()-1;
        if (nums[high] >= nums[low]) return nums[low];
        while (high - low != 1)
        {
            int mid = low + ((high-low) >> 1);
            if (nums[mid] > nums[low]) low = mid;
            else if (nums[mid] < nums[high]) high = mid;
        }
        return nums[high];
    }
};
