def my_sort(nums: list) -> list:
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
    # 全为奇数或全为偶数，无法交换，直接返回
    if even == len(nums) or even == 0:
        return nums
    # 既存在奇数，又存在偶数，快排后返回
    else:
        return sorted(nums)
    
    
    
    
lst1 = [7, 3, 5, 1]
assert my_sort(lst1) == [7, 3, 5, 1]

lst2 = [53941, 38641, 31525, 75864, 29026, 12199, 83522, 58200, 64784, 80987]
assert my_sort(lst2) == [12199, 29026, 31525, 38641, 53941, 58200, 64784, 75864, 80987, 83522]
