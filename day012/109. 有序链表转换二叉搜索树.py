# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 分治，时间复杂度O(NlogN)，空间复杂度O(logN)
        if not head:
            return
        mid = self.find_middle(head)
        node = TreeNode(mid.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
        
        
    def find_middle(self, head):
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        return slow
