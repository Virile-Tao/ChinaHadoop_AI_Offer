class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 时间复杂度O(logN)，空间复杂度O(1)
        if not nums:
            return -1
        
        first, last = 0, len(nums) - 1
        # 找到旋转的点，即first是最大值，last是最小值，last即为要旋转的点
        while last - first != 1:
            mid = (first + last) // 2
            if nums[mid] > nums[first]:
                first = mid
            elif nums[mid] < nums[last]:
                last = mid
            else:
                break
        # 二分查找
        def binary_search(lst, begin, end, target):
            while begin <= end:
                pivot = (begin + end) // 2
                if lst[pivot] < target:
                    begin = pivot + 1
                elif lst[pivot] > target:
                    end = pivot - 1
                else:
                    return pivot
            return -1
        
        # 在前半段寻找
        if nums[0] <= target <= nums[first]:
            return binary_search(nums, 0, first, target)
        # 在后半段寻找
        elif nums[last] <= target <= nums[len(nums)-1]:
            return binary_search(nums, last, len(nums)-1, target)
        else:
            return -1
