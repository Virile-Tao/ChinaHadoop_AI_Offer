# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 时间复杂度O(Nlogk)，空间复杂度O(1)，N是所有结点的个数
        # 分治法，将链表两两配对进行合并
        if not lists:
            return None
        k = len(lists) - 1
        while k != 0:
            i, j = 0, k
            while i < j:
                lists[i] = self.merge2lists(lists[i], lists[j])
                i += 1
                j -= 1
            k = k // 2
        return lists[0]
    
    def merge2lists(self, l1, l2):
        # 合并两个链表，并排序
        head = ListNode(None)
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2
        return head.next
            
    
    
    def mergeKLists_v2(self, lists: List[ListNode]) -> ListNode:
        # 时间复杂度O(NlogN)，空间复杂度O(N)，N是所有结点的个数
        # 暴力法，把所有数据取出来，快排，然后生成一个新链表
        lst = list()
        for l in lists:
            while l is not None:
                lst.append(l.val)
                l = l.next
        lst.sort()
        head = ListNode(None)
        cur = head
        for i in lst:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        return head.next
