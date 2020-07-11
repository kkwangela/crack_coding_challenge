## DP O(N^2), O(N^2)
```Python
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True 
        ans = len(s)
        for i in range(1, len(s)):
            for j in range(i - 1, -1, -1):
                #写成for j in range(i)也行，因为dp[j+1][i-1]在上一个i循环里已经计算过了
                if s[i] == s[j] and (j + 1 == i or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    ans += 1 
        return ans

```

