class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 时间复杂度O(N*M)，空间复杂度O(1)
        # 双指针同步移动
        i, j = 0, 0
        xing = None
        while i < len(s):
            # 可一一对应匹配
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            # 不可一一对应匹配，但s[j]=='*'
            elif j < len(p) and p[j] == '*':
                matched = i     # 记录s中可能要匹配的位置
                xing = j        # 记录p中*的位置
                j += 1          # 先让*匹配一个空字符，故i不加一
            # 不可一一匹配且s[j]!='*'，但xing不为None
            elif xing is not None:
                matched += 1    # 让matched对应的*多匹配一个字符
                i = matched
                j = xing + 1
            # 不可一一匹配且没有*
            else:
                return False
        if p[j:]:
            # 若p[j:]不为空，则p[j:]全为*，否则返回False   
            return len(set(p[j:])) == 1 and '*' in set(p[j:])
        else:
            return True
