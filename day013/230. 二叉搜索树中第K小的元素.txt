# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        # 中序遍历获得有序数组，返回下标k-1对应的数据即第k小的数据
        lst = list()
        def helper(root):
            if root is None:
                return
            helper(root.left)
            lst.append(root.val)
            helper(root.right)
        helper(root)
        return lst[k-1]
