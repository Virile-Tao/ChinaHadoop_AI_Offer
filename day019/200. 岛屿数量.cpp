class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        int m = grid.size();
        if (m == 0) return count;
        int n = grid[0].size();
        for (int i=0; i<m; i++)
        {
            for (int j=0; j<n; j++)
            {
                if (grid[i][j] == '1')
                {
                    count++;
                    spread(grid, i, j, m, n);
                }
            }
        }
        return count;
    }
    void spread(vector<vector<char> >& grid, int i, int j, int& m, int& n)
    {
        if (i < 0 || i > m - 1 || j < 0 || j > n - 1 || grid[i][j] == '0' || grid[i][j] == 'T') return ;
        grid[i][j] = 'T';
        spread(grid, i-1, j, m, n);
        spread(grid, i+1, j, m, n);
        spread(grid, i, j-1, m, n);
        spread(grid, i, j+1, m, n);
    }
};
