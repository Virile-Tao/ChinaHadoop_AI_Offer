# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 时间复杂度O(N)，空间复杂度O(1)
        # 快慢指针
        if not head:
            return False
        fast, slow = head, head
        while fast:
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
        
    def hasCycle_v2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 时间复杂度O(N)，空间复杂度O(N)
        # 使用哈希表存储结点的地址，如果地址有重复则存在环
        se = set()
        cur = head
        while cur:
            if cur in se:
                return True
            se.add(cur)
            cur = cur.next
        return False
