class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 时间复杂度O(i*j)，i为单词的个数，j为最短单词的长度，空间复杂度O(1)
        # 先找第一个单词和第二个单词的公共前缀，再找公共前缀与第三个单词的公共前缀，以此类推，直至遍历完整个strs
        if not strs:
            return ''
        for i in range(len(strs)):
            for j in range(len(strs[0])):
                if strs[0][:j+1] != strs[i][:j+1]:
                    strs[0] = strs[0][:j]
        return strs[0]
