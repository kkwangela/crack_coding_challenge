# Greedy + Priority Queue

Going through day1 to the end of the day x, how can we determine which event to attend at day i? We attend the event that ends first. So we need a structure that can hold available events at day i and can have easy access to the smallest number: Priority queue(heap)

```python
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        h = []
        events.sort(reverse = True)
        d = 0
        res = 0
        while h or events:
            if not h:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(h, events.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res

```
