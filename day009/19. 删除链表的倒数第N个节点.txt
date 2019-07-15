# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 时间复杂度O(N)，空间复杂度O(1)
        if head is None:
            return head
        first, last = head, head
        pre = None
        while n > 1:
            last = last.next
            n -= 1
        while last.next is not None:
            pre = first
            last = last.next
            first = first.next
        if pre is None:
            head = head.next
        else:
            pre.next = first.next
        return head
