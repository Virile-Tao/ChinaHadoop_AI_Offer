# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 时间复杂度O(N+M)，空间复杂度O(1)
        if headA is None or headB is None:
            return None
        curA, curB = headA, headB
        while True:
            if curA is curB:
                return curA
            if curA is None:
                curA = headB
                curB = curB.next
            elif curB is None:
                curB = headA
                curA = curA.next
            else:
                curA = curA.next
                curB = curB.next
            
            
            
