class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount_v2(self, S):
        # write your code here
        # 暴力法，时间复杂度O(N^3)，超时、、、
        S.sort()
        n = len(S)
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if S[i] + S[j] > S[k] and S[k] - S[j] < S[i]:
                        count += 1
        return count

    def triangleCount(self, S):
        # write your code here
        # 双指针法，参考三数之和，时间复杂度O(N^2)
        S.sort()
        n = len(S)
        count = 0
        for k in range(n-1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if S[i] + S[j] > S[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
