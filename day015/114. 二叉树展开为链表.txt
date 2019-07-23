# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def flatten(self, root: TreeNode) -> None:
        # 时间复杂度O(N)，空间复杂度最坏O(N)
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre = root.left
            while pre.right:     # 找到左子树的最右结点，这个结点将连接右子树
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None
            
    # 迭代
    def flatten_v2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while (root != None):
            if root.left != None:
                most_right = root.left
                while most_right.right != None: most_right = most_right.right
                most_right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return
