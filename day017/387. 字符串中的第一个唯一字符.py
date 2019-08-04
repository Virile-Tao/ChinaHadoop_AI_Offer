class Solution:
    def firstUniqChar_v2(self, s: str) -> int:
        # 时间复杂度O(N^2)，空间复杂度O(1)
        # 暴力法
        if s == '':
            return -1
        for i in range(len(s)):
            if s[i] in s[:i] + s[i+1:]:
                continue
            else:
                return i
        return -1
    
    def firstUniqChar(self, s: str) -> int:
        # 时间复杂度O(N)，空间复杂度O(N)
        # 使用字典存储字符串中的字符和出现的次数
        dic = dict()
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
