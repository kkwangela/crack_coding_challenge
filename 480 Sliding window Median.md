Similar to 295 Find median from data stream, we use heap. However, now we need to support "remove" functionality. So we create a class Heap, and use to heaps to do removement.
```Python
from heapq import *
class Heap:
    def __init__(self):
        self.q1 = []
        self.q2 = []
        
    def push(self, num):
        heappush(self.q1, num)
        
    def remove(self, num):
        heappush(self.q2, num)
        
    def pop(self):
        while self.q2 and self.q2[0] == self.q1[0]:
            heappop(self.q1)
            heappop(self.q2)
        if self.q1:
            heappop(self.q1)
    
    def top(self):
        while self.q2 and self.q2[0] == self.q1[0]:
            heappop(self.q1)
            heappop(self.q2)
        if self.q1:
            return self.q1[0]
    
    def size(self):
        return len(self.q1) - len(self.q2)
            
    
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        minHeap = Heap()
        maxHeap = Heap()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] <= -minHeap.top():
                minHeap.push(-nums[i])
            else:
                maxHeap.push(nums[i])
        
            if i < k - 1:
                continue 
            
            if i >= k:
                val = nums[i - k]
                if val <= -minHeap.top():
                    minHeap.remove(-val)
                else:
                    maxHeap.remove(val)
            
            if i >= k - 1:
                while minHeap.size() > maxHeap.size() + 1:
                    val = -minHeap.top()
                    minHeap.pop()
                    maxHeap.push(val)
                while maxHeap.size() > minHeap.size():
                    val = maxHeap.top()
                    maxHeap.pop()
                    minHeap.push(-val)
                if k % 2 == 1:
                    res.append(-minHeap.top())
                else:
                    res.append((maxHeap.top() - minHeap.top()) / 2.0)

        return res

```
