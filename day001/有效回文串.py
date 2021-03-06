class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
        
        
       
# 掌握.join()函数的用法，如''.join(s)，用''连接s字符串中的每个元素
# 掌握filter(fun,seq)函数的用法，对序列中的每个元素进行fun判断，判断为True的保留，并返回一个迭代器
