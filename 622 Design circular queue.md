Satrt by initializing an array of size k. We need a start and a rear variables to record the current start and rear of the queue. Since this is a circular queue, to update the index of the start and rear, use "mod" operation.
```Python
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.start = 0
        self.rear = 0
        self.array = [0] * k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.rear = (self.start + self.size) % len(self.array)
        self.array[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        res = self.array[self.start]
        self.start = (self.start + 1) % len(self.array)
        self.size -= 1 
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): 
            return -1
        return self.array[self.start]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): 
            return -1
        return self.array[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.array)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

```
