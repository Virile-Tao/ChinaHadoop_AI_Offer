# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 递归，时间复杂度O(N)，空间复杂度O(N)
        levels = []
        if not root:
            return levels
        def helper(root, level):
            if level == len(levels):
                levels.append([])
            levels[level].append(root.val)
            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)
        helper(root, 0)
        return levels
