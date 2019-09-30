class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int first = cost[0], second = cost[1], tmp;
        for (int i=2; i<cost.size(); i++)
        {
            tmp = cost[i] + (first < second ? first : second);
            first = second;
            second = tmp;
        }
        return first < second ? first : second;
    }
};
