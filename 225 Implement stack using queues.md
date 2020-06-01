Use two queues to implement a stack. One queue is responsible for storing items, the other oe helps to get the "bottom" item (top, pop operations)
```Python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
    
    def moveItems(self):
	#helper function to move items in queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
            
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.moveItems()
        res = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res
    
    def top(self) -> int:
        """
        Get the top element.
        """
        self.moveItems()
        res = self.queue1.pop(0)
        self.queue2.append(res)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

```
