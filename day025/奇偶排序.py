def my_sort(nums: list) -> list:
    for num in nums:
        # 如果存在一个偶数，直接按顺序排
        if num % 2 == 0:
            return sorted(nums)
    # 如果不存在偶数，直接返回
    return nums
    
    
    
    
lst1 = [7, 3, 5, 1]
assert my_sort(lst1) == [7, 3, 5, 1]

lst2 = [53941, 38641, 31525, 75864, 29026, 12199, 83522, 58200, 64784, 80987]
assert my_sort(lst2) == [12199, 29026, 31525, 38641, 53941, 58200, 64784, 75864, 80987, 83522]
