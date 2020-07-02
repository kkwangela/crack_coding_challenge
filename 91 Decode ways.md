## DP O(n), O(1)
dp[i] = the number of ways to decode values[0: i + 1].
dp[i] = dp[i - 1] + dp[i - 2] provided that current digit is not "0" and the previous + curretn digit is within [10, 26].

```Python
class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1 
        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

```

We can compressse the space we use to O(1):
```Python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0 for _ in range(2)]
        dp[0] = 1 
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, len(s) + 1):
            tmp = 0
            if s[i - 1] != "0":
                tmp += dp[1]
            if 10 <= int(s[i - 2: i]) <= 26:
                tmp += dp[0]
            dp[0], dp[1] = dp[1], tmp  
        return dp[1]

```


 