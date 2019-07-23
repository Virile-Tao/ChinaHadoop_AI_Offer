# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 时间复杂度O(N)，空间复杂度最坏O(N)，如果是平衡二叉树则O(logN)
        lst = []
        def helper(root, sum, path=[]):
            if root is None:
                return
            if root.left is None and root.right is None:
                if root.val == sum:
                    lst.append(path+[root.val])
                return
            elif root.left is None and root.right is not None:
                helper(root.right, sum - root.val, path+[root.val])
            elif root.left is not None and root.left is None:
                helper(root.left, sum - root.val, path+[root.val])
            else:
                helper(root.left, sum - root.val, path+[root.val])
                helper(root.right, sum - root.val, path+[root.val])
        helper(root, sum)
        return lst
    
    
    def pathSum_v2(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root: return []
        def helper(root,sum, tmp):
            if not root:
                return 
            if not root.left and not root.right and sum - root.val == 0 :
                tmp += [root.val]
                res.append(tmp)
                return 
            helper(root.left, sum - root.val, tmp + [root.val])
            helper(root.right, sum - root.val, tmp + [root.val])
        helper(root, sum, [])
        return res
