class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 时间复杂度最坏O(N)，空间复杂度O(1)
        if not nums:
            return False
        n = len(nums)
        # (1)首，尾，目标相等，直接返回True
        if nums[0] == nums[n-1] and nums[0] == target:
            return True
        
        # (2)首尾相等，但与目标不等，顺序查找
        if nums[0] == nums[n-1]:
            for num in nums:
                if num == target:
                    return True
            return False
            
        # (3)首，尾不等，与目标也不等，二分查找
        def binary_search(lst, begin, end, target):
            while begin <= end:
                pivot = (begin + end) // 2
                if lst[pivot] > target:
                    end = pivot - 1
                elif lst[pivot] < target:
                    begin = pivot + 1
                else:
                    return True
            return False
        first, last = 0, n-1
        # (3.1)若没有旋转，直接二分查找
        if nums[first] < nums[last]:
            return binary_search(nums, first, last, target)
        # (3.2)若旋转了，找到分割点
        while last - first != 1:
            mid = (first + last) // 2
            if nums[mid] >= nums[first]:
                first = mid
            elif nums[mid] <= nums[last]:
                last = mid
        # (3.2.1)在左侧二分查找
        if nums[0] <= target <= nums[first]:
            return binary_search(nums, 0, first, target)
        # (3.2.2)在右侧二分查找
        elif nums[last] <= target <= nums[n-1]:
            return binary_search(nums, last, n-1, target)
        else:
            return False
        
                
