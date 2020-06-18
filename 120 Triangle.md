## DP - bottom up
```Python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            new_dp = []
            row = triangle[i]
            for j in range(len(row)):
                cur = min(row[j] + dp[j], row[j] + dp[j + 1])
                new_dp.append(cur)
            dp = new_dp
        return dp[0]

```
