class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        三种方法
        （1）快排后遍历找重复
        （2）哈希映射找重复
        （3）快慢指针，看了很久才看懂，后面好好消化一下
        '''
        # 时间复杂度O(N)，空间复杂度O(1)
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        p1, p2 = nums[0], slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
    
    def findDuplicate_v2(self, nums: List[int]) -> int:
        # 时间复杂度O(NlogN)，空间复杂度O(1)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
            
    def findDuplicate_v3(self, nums: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        se = set()
        for num in nums:
            if num in se:
                return num
            se.add(num)
