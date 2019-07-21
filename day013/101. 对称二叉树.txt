# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 时间复杂度O(N)，空间复杂度O(N)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        l = self.isMirror(p.left, q.right)
        r = self.isMirror(p.right, q.left)
        return p.val == q.val and l and r
        
