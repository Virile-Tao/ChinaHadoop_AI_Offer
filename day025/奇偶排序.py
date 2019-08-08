import sys


def fun():
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
    # 全为奇数或全为偶数，无法交换，直接返回
    if even == len(nums) or even == 0:
        return ' '.join(map(str, nums))
    # 既存在奇数，又存在偶数，快排后返回
    else:
        nums.sort()
        return ' '.join(map(str, nums))


if __name__ == '__main__':
    assert fun() == '7 3 5 1'
    assert fun() == '12199 29026 31525 38641 53941 58200 64784 75864 80987 83522'
    assert fun() == '8 4 6 10'

# 输入 7 3 5 1 输出 7 3 5 1 
# 输入 53941 38641 31525 75864 29026 12199 83522 58200 64784 80987 输出 12199 29026 31525 38641 53941 58200 64784 75864 80987 83522
# 输入 8 4 6 10 输出 8 4 6 10
