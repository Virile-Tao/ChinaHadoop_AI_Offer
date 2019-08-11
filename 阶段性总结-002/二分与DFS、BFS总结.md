## 面试中常见的时间复杂度
比O(N)更优的时间复杂度只能是O(logN)的二分
## 二分
### 基本思想
一分为二，查找，再一分为二查找，直至找到
### 代码实现
```python
# 非递归
def binary_search(nums, low, high, value):
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < value:
            low = mid + 1
        elif nums[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1
# 递归
def binary_search(nums, low, high, value):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] < value:
        return binary_search(nums, mid + 1, high, value)
    elif nums[mid] > value:
        return binary_search(nums, low, mid - 1, value)
    else:
        return mid
```
## 递归
### 什么是递归
函数自己调用自己。Recursion是代码的实现方式，并不能算是一种算法。递归就是当多重循环层数不确定的时候，一个更优雅的实现多重循环的方式。
```python
def recursion(self, n, visited, path):
    if len(path) == n:
        # do something
        return
    
    for i in range(1, n+1):
        if i not in visited:
            path.append(i)
            self.recursion(n, visited, path)
            path.pop()
```
### 递归三要素
> * 递归的定义
> * 递归的拆解
> * 递归的出口
## DFS与BFS
### DFS
碰到找所有方案的题，基本可以确定是DFS。除了二叉树以外的90%DFS的题，幺妹是排列，要么是组合
### BFS
#### 什么时候用
> * 图的遍历：
1.层级遍历
2.由点及面
3.拓扑排序
> * 最短路径
> * 非递归的方式找所有方案
#### 二叉树上的宽度优先搜索
使用队列最为主要的数据结构 queue
