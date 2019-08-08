import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 空间复杂度O(N)
        self.lst = list()
        self.dic = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # 时间复杂度O(1)
        if val in self.dic:
            return False
        else:
            self.dic[val] = len(self.lst)
            self.lst.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # 时间复杂度O(1)
        if val not in self.dic:
            return False
        else:
            self.dic[self.lst[-1]] = self.dic[val]
            self.lst[self.dic[val]] = self.lst[-1]
            self.lst.pop()
            self.dic.pop(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # 时间复杂度O(1)
        return self.lst[random.randint(0, len(self.lst) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
