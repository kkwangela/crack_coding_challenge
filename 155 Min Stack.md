Use two stacks. One to record items, the other one to record current minimum number. When we pop an item, we need to also check if it is the current min elemet in stack2. If so, pop it out as well.
```Python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        
        self.stack1.append(x)
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)
    def pop(self) -> None:
        if self.stack1.pop() == self.stack2[-1]:
            self.stack2.pop()
            

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]

```
