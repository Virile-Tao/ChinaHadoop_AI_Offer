class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, 0);
        for (int i=1; i<=amount; i++)
        {
            int tmp = amount + 1;
            for (int coin : coins)
            {
                if (i - coin < 0) continue;
                tmp = tmp < dp[i - coin] ? tmp : dp[i - coin];
            }
            dp[i] = tmp + 1;
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
