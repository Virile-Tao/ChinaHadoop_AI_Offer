# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 时间复杂度O(N)，空间复杂度O(N)
    # 初始化一个变量用于记录最近的公共节点
    # 递归调用，如果左节点是p或q，则left为True，如果右节点是p或q，则right为True，如果自己是p或q，则flag为True
    def __init__(self):
        self.res = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return False
            
            left = helper(node.left)
            right = helper(node.right)
            
            flag = False
            if p is node or q is node:
                flag = True
                
            if left + right + flag >= 2:
                self.res = node
            
            return left or right or flag
            
        helper(root)
        return self.res
