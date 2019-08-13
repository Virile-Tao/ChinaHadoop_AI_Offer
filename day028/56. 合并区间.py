class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 时间复杂度O(NlogN)，空间复杂度O(N)
        # 按元素的第一个值进行排序，然后遍历合并区间
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for num in intervals[1:]:
            if res[-1][1] >= num[0]:
                res[-1][1] = max(num[1], res[-1][1])
            else:
                res.append(num)
        return res
