class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 时间复杂度O(NlogN)，空间复杂度O(1)
        nums.sort()
        return nums[-k]
    
    def findKthLargest_v2(self, nums: List[int], k: int) -> int:
        # 时间复杂度O(Nlogk)，空间复杂度O(k)
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_v2(self, nums: List[int], k: int) -> int:
        # 时间复杂度O(Nlogk)，空间复杂度O(k)
        # 大数据量，且内存不足时，使用最小堆数据结构
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
