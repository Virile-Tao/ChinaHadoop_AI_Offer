class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 时间复杂度O(NlogK)，空间复杂度O(K)
        # 二分插排
        q = [float('inf')] * k
        for mat in matrix:
            for i in mat:
                bisect.insort(q, i, hi = k)
                q.pop()
        return q[-1]
