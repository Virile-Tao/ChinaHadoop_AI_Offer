class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 1) return 0;
        int maxProfit = 0, curProfit = 0, minPrice = prices[0];
        for (int i=1; i<prices.size(); i++)
        {
            if (prices[i] < minPrice)
            {
                minPrice = prices[i];
                continue;
            }
            curProfit = prices[i] - minPrice;
            maxProfit = maxProfit > curProfit ? maxProfit : curProfit;
        }
        return maxProfit;
    }
};
