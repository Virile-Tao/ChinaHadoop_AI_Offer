class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 时间复杂度O(N)，空间复杂度O(1)
        # 双指针法
        left, right = 0, len(arr) - 1
        while right - left + 1 != k:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
        return arr[left:right+1]
            
    
    def findClosestElements_v2(self, arr: List[int], k: int, x: int) -> List[int]:
        # 时间复杂度O(KN)，空间复杂度O(K)
        # 太暴力，二分查找得到最近元素后，将相邻元素依次遍历添加到列表中
        def binary_search(arr, x):
            first, last = 0, len(arr) - 1
            while first <= last:
                mid = (first + last) // 2
                if x > arr[mid]:
                    first = mid + 1
                elif x < arr[mid]:
                    last = mid - 1
                else:
                    return mid
            if first == -1:
                return last
            if last == len(arr):
                return first
            return first if abs(x - arr[first]) < abs(x - arr[last]) else last
        # 返回与x差值最小的元素下标
        index = binary_search(arr, x)
        lst = [arr[index]]
        count = 1
        index_left = index - 1
        index_right =  index + 1
        for _ in range(k-1):
            if 0 <= index_right <= len(arr) - 1 and 0 <= index_left <= len(arr) - 1:
                if abs(arr[index_right] - x) < abs(arr[index_left] - x):
                    lst.append(arr[index_right])
                    index_right += 1
                else:
                    # abs(arr[index_right] - x) => abs(arr[index_left] - x)
                    lst.insert(0, arr[index_left])
                    index_left -= 1
            elif index_right == len(arr):
                lst.insert(0, arr[index_left])
                index_left -= 1
            elif index_left == -1:
                lst.append(arr[index_right])
                index_right += 1
        return lst
