# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 时间复杂度O(N)，空间复杂度O(1)
        if not head:
            return head
        pre = None
        cur = head
        temp = m
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
        first = pre
        last = cur
        while (n - temp) >= 0:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
            n -= 1
        if not first:
            head = pre
        else:
            first.next = pre
        last.next = cur
        return head
