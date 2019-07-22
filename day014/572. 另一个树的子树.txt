# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 时间复杂度O(N)，空间复杂度O(N)，最坏的情况压栈N次
    # （1）s和t是否相等，isEqual(l,r)判断s和t是否完全相同
    # （2）t是否是s左子树的子树
    # （3）t是否是s右子树的子树
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val == t.val:
            return self.isEqual(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isEqual(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        if l.val == r.val:
            return self.isEqual(l.left, r.left) and self.isEqual(l.right, r.right)
        return False
