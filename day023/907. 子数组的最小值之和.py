class Solution:
    def sumSubarrayMins_v2(self, A: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        # 一遍遍历
        ans = 0
        A = [float('-inf')] + A + [float('-inf')]
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                ans += A[cur] * (i-cur) * (cur-stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)
    
    def sumSubarrayMins(self, A: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        # 两遍遍历
        len_A = len(A)
        if len_A == 0:
            return 0
        if len_A == 1:
            return A[0]
        
        ans = 0
        left = [0] * len_A
        right = [0] * len_A
        
        stack = []
        for i in range(len_A):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(len_A - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if not stack:
                right[i] = len_A
            else:
                right[i] = stack[-1]
            stack.append(i)
        
        for i in range(len_A):
            ans += (i - left[i]) * (right[i] - i) * A[i]
            ans %= 1000000007
        return ans
