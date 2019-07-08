class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 时间复杂度O(n)，遍历一次列表；空间复杂度O(1)，不需额外存储空间
        # 如果没有旋转排序树组，直接返回nums[0]，如果旋转，则找到num[i+1]<num[i]，返回num[i+1]
        for i in range(len(nums)):
            if len(nums) == i+1:
                return nums[0]
            if nums[i+1] > nums[i]:
                continue
            else:
                return nums[i+1]
