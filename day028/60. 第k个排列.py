class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 时间复杂度O(2^N)，空间复杂度O(N+K)
        # 回溯 + 剪枝
        # 如果 k 大于这一个分支将要产生的叶子结点数，直接跳过这个分支，即“剪枝”
        # 如果 k 小于等于这一个分支将要产生的叶子结点数，那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解
        nums = [i for i in range(1, n+1)]
        used = [False for i in range(n)]
        res = self.dfs(nums, used, n, k, 0, [])
        print(res)
        res = map(str, res)
        return ''.join(res)
        
    def factorial(self, n):
        temp = 1
        for _ in range(1, n):
            temp *= n
            n -= 1
        return temp
        
    def dfs(self, nums, used, n, k, depth, res):
        if depth == n:
            return res
        fac = self.factorial(n - depth - 1)
        for i in range(n):
            if used[i]:
                continue
            if k > fac:
                k -= fac
                continue
            res.append(nums[i])
            used[i] = True
            return self.dfs(nums, used, n, k, depth + 1, res)
