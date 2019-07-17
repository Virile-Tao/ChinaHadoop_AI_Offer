# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 时间复杂度O(NlogN)，空间复杂度O(1)
        # 快排
        newHead = ListNode(0)
        newHead.next = head
        self.quicksort(newHead, None)
        return newHead.next

    def partition(self, start, end):
        node = start.next.next
        pivotPrev = start.next
        pivotPrev.next = end
        pivotPost = pivotPrev
        while node != end:
            temp = node.next
            if node.val > pivotPrev.val:
                node.next = pivotPost.next
                pivotPost.next = node
            elif node.val < pivotPrev.val:
                node.next = start.next
                start.next = node
            else:
                node.next = pivotPost.next
                pivotPost.next = node
                pivotPost = pivotPost.next
            node = temp
        return [pivotPrev, pivotPost]

    def quicksort(self, start, end):
        if start.next != end:
            prev, post = self.partition(start, end)
            self.quicksort(start, prev)
            self.quicksort(post, end)
        

class Solution_v2:
    def sortList(self, head: ListNode) -> ListNode:
        # 时间复杂度O(NlogN)，空间复杂度O(N)
        # 归并排序
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        mid = None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        
        h = res = ListNode(None)
        while left and right:
            if left.val <= right.val:
                h.next = left
                h = h.next
                left = left.next
            else:
                h.next = right
                h = h.next
                right = right.next
        if left:
            h.next = left
        if right:
            h.next = right
        return res.next




列表或数组的快排实现，复习一下
# 快排
def quick_sort(self, lst, first, last):
    if first >= last:
        return
    low, high = first, high
    pivot = lst[first]
    while low < high:
        while low < high and lst[high] >= pivot:
            high -= 1
        lst[low] = lst[high]
        while low < high and lst[low] <= pivot:
            low += 1
        lst[high] = lst[low]
    lst[low] = pivot

    quick_sort(lst, first, low-1)
    quick_sort(lst, high+1, last)
