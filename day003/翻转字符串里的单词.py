class Solution:
    def reverseWords(self, s: str) -> str:
        # 时间复杂度O(n)，空间复杂度O(m)，n是字符串中单词个数，m为单词的个数
        # 用split( )函数将字符串划分为若干个单词，再反向拼接
        s = s.split( )
        temp = ''
        for i in s[::-1]:
            temp = temp + ' ' + i
        return temp.strip()
