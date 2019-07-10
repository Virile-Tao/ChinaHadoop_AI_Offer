class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 0      # 记录结点左边有多少个结点（元素）

class Solution:
    # 时间复杂度O(N)，空间复杂度O(N)
    '''
    构建二叉搜索树，左边结点元素小于根结点，右边大于根结点，
    每个结点有个属性count记录左边结点个数，res为最后输出的数组
    倒序插入二叉搜索树，若比根结点小，根结点count++，若比根结点大则数组res[i]+=root.count+1
    '''
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        root = None
        for i in range(len(nums)-1, -1, -1):         # 倒序插入二叉搜索树
            root = self.insertNode(root, i, nums[i], res)
        return res
        
    def insertNode(self, root, i, val, res):
        if root is None:
            root = Node(val)
        elif val <= root.val:
            root.count += 1
            root.left = self.insertNode(root.left, i, val, res)
        elif val > root.val:
            res[i] = res[i] + root.count + 1
            root.right = self.insertNode(root.right, i, val, res)
        return root
    
    
    
    def countSmaller_v2(self, nums: List[int]) -> List[int]:
        # 暴力法，时间复杂度O(N^2)，空间复杂度O(N)
        lst = list()
        for i in range(len(nums)):
            lst.append(len([nums[j] for j in range(i+1, len(nums)) if nums[j] < nums[i]]))
        return lst
