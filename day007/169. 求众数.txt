class Solution:
    '''
    两种方法：
    （1）哈希映射计算众数
    （2）快排后直接返回中位数
    '''
    def majorityElement(self, nums: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        n = len(nums)
        setEle = set(nums)
        for ele in setEle:
            if nums.count(ele) > n/2:
                return ele
            
            
            
    def majorityElement_v2(self, nums: List[int]) -> int:
        # 时间复杂度O(NlogN)，空间复杂度O(N)
        nums.sort()
        return nums[len(nums)//2]
