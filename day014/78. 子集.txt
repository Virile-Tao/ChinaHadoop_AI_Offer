class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 时间复杂度O(N^2)，空间复杂度O(N^2)
        # nums中前k个数构成子集set，第k+1个数放入set的每个元素中则构成k+1个数的子集
        lst = [[]]
        for num in nums:
            temp = [[num] + i for i in lst]
            lst.extend(temp)
        return lst
