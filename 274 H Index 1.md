## Sort and search O(NlogN)
Since the given array is unsorted, we can firstly sort it and then do linear search or binary search. Sorting is O(NlogN), so either either linear search or binary search will not affect the final complexity.
```Python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0

```

## Bucket sort O(N)
Trade space complexity with time complexity! Create a buckted from 0 to n + 1 (n = len(arr)), and put all papers with citations >= n to the last bucket, and the rest in the corresponding bucket. (Bucket[i] means how many of the paper are cited i times). Then, start search from the last bucket until we find a bucket that the number of papers have citations >= bucket[i] is larger or equal to i.
```Python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        bucket = [0 for _ in range(n + 1)]
        for c in citations:
            if c >= n:
                bucket[n] += 1 
            else:
                bucket[c] += 1 
        
        suffix = 0
        for i in range(len(bucket) - 1, -1, -1):
            suffix += bucket[i]
            if suffix >= i:
                return i

```
