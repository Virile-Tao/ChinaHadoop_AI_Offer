class Solution:
    def isValid(self, s: str) -> bool:
        # 时间复杂度O(N)，空间复杂度O(N)
        lst = list()
        for i in s:
            if len(lst) == 0:
                lst.append(i)
            elif ord(i)-ord(lst[-1]) == 1 or ord(i)-ord(lst[-1]) == 2:
                lst.pop()
            else:
                lst.append(i)
        return True if len(lst) == 0 else False
