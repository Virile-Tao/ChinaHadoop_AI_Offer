import math
class Solution:
    def reachNumber(self, target: int) -> int:
        # 时间复杂度O(1)，空间复杂度O(1)
        target = abs(target)
        a = math.sqrt(2 * target + 0.25) - 0.5
        if a == int(a):
            return int(a)
        else:
            a = int(a) + 1
            if ((a + 1) // 2) % 2 == target % 2:
                return a
            elif a % 2 == 1:
                return a + 2
            else:
                return a + 1
