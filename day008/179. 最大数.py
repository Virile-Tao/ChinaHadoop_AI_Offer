class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 时间复杂度O(N^2)，空间复杂度O(1)
        # 对冒泡排序的一个改进
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if str(nums[j]) + str(nums[j + 1]) > str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        res = ''
        for i in nums:
            res = str(i) + res
        return res if res[0] != '0' else '0'
        
        
        
# 后面尝试使用快排，改进上述算法




# 作弊的做法：
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
