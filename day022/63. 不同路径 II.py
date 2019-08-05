class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 时间复杂度O(mn)，空间复杂度O(1)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        
        # 填充第一列
        for i in range(1, m):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i-1][0]
        # 填充第一行
        for i in range(1, n):
            obstacleGrid[0][i] = 0 if obstacleGrid[0][i] == 1 else obstacleGrid[0][i-1]
            
        # obstacleGrid[1][1]开始
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1] if obstacleGrid[i][j] == 0 else 0
                
        # print(obstacleGrid)
        return obstacleGrid[m-1][n-1]
            
        
