在这个网站做的题：
https://www.lintcode.com/problem/convert-binary-tree-to-linked-lists-by-depth/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        # 时间复杂度O(N^2)，空间复杂度O(N)
        # 思路：二叉树的层级遍历
        levels = list()
        def helper(root, level):
            if root is None:
                return
            if level == len(levels):
                levels.append(ListNode(root.val))
            else:
                cur = levels[level]
                while cur.next:
                    cur = cur.next
                cur.next = ListNode(root.val)
            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)
        helper(root, 0)
        return levels
