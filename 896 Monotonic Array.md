If two consecutive numbers are equal, it will not affect the monotony of the arr, so we could leave it there, and consider only the case they are not equal.
```Python
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return True
        incr = False 
        decr = False
        for i in range(1, len(A)):
            if A[i] - A[i - 1] > 0:
                incr = True 
            elif A[i] - A[i - 1] < 0:
                decr = True
            if incr and decr:
                return False 
        return True

```
