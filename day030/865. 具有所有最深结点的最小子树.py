# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 时间复杂O(N)，空间复杂度O(N)
        # 深度优先遍历，遍历两遍
        # 第一遍记录每个结点对应的深度，第二遍寻找最大深度的结点
        # 若左右结点均为最大深度，则返回该结点，若左右有一个具有最大深度，也返回该结点
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
                        
        dfs(root)
        max_depth = max(depth.values())
        
        def answer(node):
            if not node or depth[node] == max_depth:
                return node
            left = answer(node.left)
            right = answer(node.right)
            return node if left and right else left or right
                        
        return answer(root)
