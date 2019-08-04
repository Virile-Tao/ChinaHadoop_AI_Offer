class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 时间复杂度O(NlogN)，空间复杂度O(1)
        # 快排
        if not nums:
            return 0
        nums.sort()
        temp = 1
        long = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                temp += 1
                long = max(long, temp)
            else:
                temp = 1
        return long
                
    def longestConsecutive(self, nums: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        # 哈希表
        if not nums:
            return 0
        se = set(nums)
        temp = 1
        long = 1
        for num in nums:
            if num - 1 not in se:
                while num + 1 in se:
                    temp += 1
                    long = max(temp, long)
                    num += 1
                temp = 1
        return long
            
