Similar to Longest Increasing Seuqnce. One trick is to first sort envelopes: increasing in its first dimension and dereasing in its second dimension, so that when you visit each envelope, at least we can make sure its width is non-decreasing. 
Why sort the second dimension to be decreasing? Consider the case (1, 2), (1, 3). If they are sorted like this then (1, 3) will be able to include (1, 2), which is not desirable. So we put (1, 3) in front of (1, 2) to avoid such problem.
```Python
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        height = [envelopes[i][1] for i in range(len(envelopes))]
        if not envelopes:
            return 0
        if len(envelopes) == 1:
            return 1
        dp = [0] * (len(envelopes) + 1)
        dp[1] = height[0]
        length = 1
        for i in range(1, len(height)):
            if height[i] > dp[length]:
                length += 1 
                dp[length] = height[i]
            else:
                index = bisect.bisect_left(dp, height[i], 1, length)
                dp[index] = min(height[i], dp[index])
            
        return length

```
