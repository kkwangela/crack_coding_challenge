## DP O(N^2)
DP[i][j] = the minimum cost of match s1[:i+1] and s2[j+1].
If s1[i-1] == s2[j-1]: dp[i][j] = dp[i - 1][j - 1]
else:
dp[i][j] = min(dp[i -1][j] + ord(s[i -1]), dp[i][j - 1] + ord(s2[j - 1]))
```Python
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
            
        
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
                
        return dp[-1][-1]      

```
