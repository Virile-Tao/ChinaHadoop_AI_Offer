# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 时间复杂度O(N)，空间复杂度O(1)
        if head is None:
            return head
        while head.val == val:
            head = head.next
            if head is None:
                break
        pre, cur = None, head
        while cur is not None:
            if cur.val == val:
                cur = cur.next
                pre.next = cur
                continue
            pre = cur
            cur = cur.next
        return head
