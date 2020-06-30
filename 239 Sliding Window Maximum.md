## 单调双端队列
试想：如果进来的数小于队内的数，那么它还有可能未来成为某个区间的最大值，如果它大于队内的数，那么队首的数永远不会成为最大值。所以要保证队列一直单调递减，并且队首是当前区间的最大值。
```Python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return []
        
        queue = collections.deque([])
        for i in range(k):
            self.enqueue(nums, queue, i)
        
        res = [nums[queue[0]]]
        for i in range(k, len(nums)):
            self.remove(queue, i - k)
            self.enqueue(nums, queue, i)
            res += [nums[queue[0]]]
        
        return res 
    
    def enqueue(self, nums, queue, index):
        while queue and nums[queue[-1]] < nums[index]:
            queue.pop()
        queue.append(index)
    
    def remove(self, queue, index):
        if queue[0] == index:
            queue.popleft()

```
