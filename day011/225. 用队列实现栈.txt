# 用两个队列模拟栈
# 时间复杂度O(N)，空间复杂度O(N)
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = list()
        self.queue2 = list()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        x = self.queue1.pop(0)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        x = self.queue1[0]
        self.queue2.append(self.queue1.pop(0))
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.queue1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
