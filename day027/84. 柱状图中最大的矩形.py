class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        # 元素依次压栈，当a[i-1]>a[i]，开始弹栈，直到a[stack[j]]≤a[i]，面积为(i−stack[top−1]−1)×a[stack[top]]
        # 当所有元素均已入栈，开始弹栈，面积为(stack[top]−stack[top−1])×a[stack[top]]
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area
    
    
    def largestRectangleArea_v2(self, heights: List[int]) -> int:
        # 时间复杂度O(NlogN)，空间复杂度O(N)
        # 分治法，超时
        def helper(nums, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if nums[min_index] > nums[i]:
                    min_index = i
            left = helper(nums, start, min_index - 1)
            right = helper(nums, min_index + 1, end)
            return max(nums[min_index] * (end - start + 1), max(left, right))
        
        return helper(heights, 0, len(heights) - 1)
    
    
    def largestRectangleArea_v3(self, heights: List[int]) -> int:
        # 时间复杂度O(N^2)，空间复杂度O(1)
        # 暴力法，超时
        n = len(heights)
        max_area = 0
        for i in range(n):
            area = heights[i]
            for left in heights[:i][::-1]:
                if left < heights[i]:
                    break
                area += heights[i]
            for right in heights[i+1:]:
                if right < heights[i]:
                    break
                area += heights[i]
            max_area = max(max_area, area)
        return max_area
