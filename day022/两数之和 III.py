class TwoSum:
    """
    @param number: An integer
    @return: nothing
    时间复杂度O(N)，空间复杂度O(N)
    """
    def __init__(self):
        self.lst = list()
        self.dic = dict()
    
    def add(self, number):
        # write your code here
        self.lst.append(number)
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.lst:
            if value - num == num:
                return self.dic[num] > 1
            else:
                if value - num in self.dic:
                    return True
        return False
