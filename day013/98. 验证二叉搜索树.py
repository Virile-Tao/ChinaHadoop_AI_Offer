# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 时间复杂度O(N)，空间复杂度O(N)
        # 中序遍历，如果中序遍历是个有序数组，则是二叉搜索树（二叉排序树）
        lst = list()
        def helper(root):
            if root is None:
                return
            helper(root.left)
            lst.append(root.val)
            helper(root.right)
        helper(root)
        for i in range(1, len(lst)):
            if lst[i] <= lst[i-1]:
                return False
        return True
    
    def isValidBST_v2(self, root: TreeNode) -> bool:
        # 时间复杂度O(N)，空间复杂度O(N)
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root)
        
        
