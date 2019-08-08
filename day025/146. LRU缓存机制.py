# 使用顺序字典模拟LRU缓存机制
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        # 空间复杂度哦O(N)
        self.ordered_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 时间复杂度O(1)
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
            return self.ordered_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 时间复杂度O(1)
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        self.ordered_dict[key] = value
        if len(self.ordered_dict) > self.capacity:
            self.ordered_dict.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
