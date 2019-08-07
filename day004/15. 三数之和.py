class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 时间复杂度O(n^2)；空间复杂度O(n)，存储满足条件的元素
        '''
        先按顺序排好，选一个数nums[k]，再寻找其余两个与它加起来满足题意的数
        （1）如果第一个元素大于0，返回空列表
        （2）如果nums[k]与前一个数相同，则无须再次寻找，跳过即可
        （3）如果和nums[k]+nums[i]+nums[j]大于0，则右移j；如果和小于0，则左移i
        （3）直至和为0，添加到列表，同时更新i，j
        '''
        nums.sort()
        lst = list()
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            if k > 0 and nums[k-1] == nums[k]: continue
            i, j = k+1, len(nums)-1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    lst.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return lst
