class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0) return false;
        int m = matrix.size();
        int n = matrix[0].size();
        int low = 0;
        int high = m*n - 1;
        while (low <= high)
        {
            int mid = low + ((high - low) >> 1);
            if (matrix[mid/n][mid%n] < target)
            {
                low = mid + 1;
            }
            else if (matrix[mid/n][mid%n] > target)
            {
                high = mid - 1;
            }
            else return true;
        }
        return false;
    }
};
