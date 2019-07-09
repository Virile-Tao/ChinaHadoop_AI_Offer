class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 时间复杂度O(logm*n)，空间复杂度O(1)
        '''
        （1）二分查找
        （2）将二维数组看做一维排序数组，中间数据为matrix[mid//n][mid%n]
        '''
        if not matrix:
            return False
        if not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (high + low) // 2
            ele = matrix[mid//n][mid%n]
            if ele == target:
                return True
            elif target < ele:
                high = mid - 1
            else:
                low = mid + 1
        return False
