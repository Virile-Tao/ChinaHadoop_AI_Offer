# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        if not root:
            return 0
        height_left = self.maxDepth(root.left)
        height_right = self.maxDepth(root.right)
        return max(height_left, height_right) + 1
