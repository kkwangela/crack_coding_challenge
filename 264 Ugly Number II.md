How to generate all ugly numbers? By multiply 2, 3, 5 by existed ugly numbers.
Use a heap to store ugly numbers, and pop out to find the next ugly numbers. To avoid duplicates, we use a set to check if an ugly number already existed.
```Python
from heapq import *
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0 :
            return 0
        heap = [1]
        primes = [2, 3, 5]
        heapify(heap)
        #res = []
        visited = set()
        visited.add(1)
        for i in range(n):
            cur = heappop(heap)
            #res.append(cur)
            for p in primes:
                if p * cur in visited:
                    continue 
 
                heappush(heap, p * cur)
                visited.add(p * cur)
        return cur

```
