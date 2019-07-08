class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 时间复杂度O(n)，一次遍历列表，空间复杂度O(n)，需要一个字典存储n个元素
        # 将列表的值和对应的索引存入字典中，利用hash查找target-num[i]是否存在
        dic = dict()
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dic:
                return [dic.get(val), i]
            dic[nums[i]] = i
