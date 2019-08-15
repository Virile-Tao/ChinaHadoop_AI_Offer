class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # 时间复杂度O(KN^2)，空间复杂度(KN^2)
        # 动态规划 probability[i][j][k]，第i步在j，k位置上的概率
        # 跳到右上角60°方位 probability[i+1][j+1][k+2] = probability[i][j][k] * 1 / 8
        # 跳到右上角30°方位 probability[i+1][j+2][k+1] = probability[i][j][k] * 1 / 8
        # 跳到右下角30°方位 probability[i+1][j+2][k-1] = probability[i][j][k] * 1 / 8
        # 跳到右下角60°方位 probability[i+1][j+1][k-2] = probability[i][j][k] * 1 / 8
        # 左边以此类推
        probability=[[[0 for _ in range(N)] for _ in range(N)] for _ in range (K+1)]
        probability[0][r][c]=1
        for i in range(K):
            for j in range(N):
                for k in range(N):
                    if probability[i][j][k]:
                            if -1<j+1<N and -1<k+2<N:
                                probability[i+1][j+1][k+2]+=probability[i][j][k]*0.125
                            if -1<j+2<N and -1<k+1<N:
                                probability[i+1][j+2][k+1]+=probability[i][j][k]*0.125
                            if -1<j+2<N and -1<k-1<N:
                                probability[i+1][j+2][k-1]+=probability[i][j][k]*0.125
                            if -1<j+1<N and -1<k-2<N:
                                probability[i+1][j+1][k-2]+=probability[i][j][k]*0.125
                            if -1<j-1<N and -1<k-2<N:
                                probability[i+1][j-1][k-2]+=probability[i][j][k]*0.125
                            if -1<j-2<N and -1<k-1<N:
                                probability[i+1][j-2][k-1]+=probability[i][j][k]*0.125
                            if -1<j-2<N and -1<k+1<N:
                                probability[i+1][j-2][k+1]+=probability[i][j][k]*0.125
                            if -1<j-1<N and -1<k+2<N:
                                probability[i+1][j-1][k+2]+=probability[i][j][k]*0.125
        p=0
        for i in range(N):
            for j in range(N):
                p+=probability[K][i][j]
        return p
