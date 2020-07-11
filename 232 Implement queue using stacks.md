Use two stacks to implement a queue. 
As what we did in "implementing stack using two queues", one stack is to store added items and the other is to help with pop, top operations. However, we can improve it: when we pop items, we move items in stack1 to stack2, and now in the stack2 the items are listed in a reversed order, so if we need to further pop or top, we can directly pop from stack2. So we can skip the step of move items back to stack1. 
```Python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        
    def moveItems(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            return self.stack2.pop()
        self.moveItems() 
        return self.stack2.pop()
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        self.moveItems()
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack2) + len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

```
