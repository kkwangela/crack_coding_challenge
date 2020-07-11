## Binary search O(logN)
Since the given arry is sorted, we can use binary search to find the **last element** in the arr that has more citation than the number of papers after that index.
Pay special attention to the case [0].
```Python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        n = len(citations)
        left, right = 0, len(citations) -1
        while left + 1 < right:
            mid = (left + right) // 2 
            if citations[mid] > n - mid:
                right = mid 
            elif citations[mid] < n - mid:
                left = mid 
            else:
                return n - mid
        
        if citations[left] >= n - left:
            return n - left
        elif citations[right] >= n - right:
            return n - right
        else: #特殊判断：[0]
            return 0

```

## Linear search O(N)
```Python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0 
        
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0

```

