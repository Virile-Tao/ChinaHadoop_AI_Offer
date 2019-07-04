class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
#         时间复杂度O(n)，空间复杂度O(n)
#         如果长度不等，直接返回False
        if len(A) != len(B):
            return False
#         如果A,B相等，则看A中有无重复的字符，若有，交换重复字符则满足题目要求，返回True；否则返回False
        if A == B:
            for i in A:
                if A.count(i) > 1:
                    return True
            return False
#         若A,B长度相等，但内容不同，则看A,B不同字符所对应的索引是否相同，并且不同的字符只能有两个，相同则返回True
        else:
            lst = [(i, j) for i, j in zip(A, B) if i!=j]
            if lst[0] == lst[1][::-1] and len(lst) == 2:
                return True
            return False
        
                
