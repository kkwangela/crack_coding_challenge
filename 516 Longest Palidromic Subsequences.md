## Method1: DP
dp[i][j] = max length of palidromic subsequence in s[i:j + 1].
```Python
if s[i] = s[j]:
    dp[i][j] = dp[i + 1][j - 1] + 2
else:
    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) 
```
Since dp[i][j] relies on dp[i+1], we need to loop reversely from the end of s to the start of s.
```Python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)- 1, -1, -1):
            for j in range(i, len(s)):
                if j == i:
                    dp[i][i] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]

```

## DFS with memo
Similar idea with dp. Instead, start from the leftmost and rightmost of s. To aoid stackoverflow, use a memo to record the result from [i, j].
```Python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return self.dfs(s, 0, len(s) - 1, {}, 0)
    
    def dfs(self, s, start, end, memo, length):
        if start == end:
            return 1
        if start > end:
            return 0
        if (start, end) in memo:
            return memo[(start, end)]
        memo[(start, end)] = 0
        if s[start] == s[end]:
            memo[(start, end)] = 2 + self.dfs(s, start + 1, end - 1, memo, length)
        else:
            memo[(start, end)] = max(self.dfs(s, start + 1, end, memo, length), self.dfs(s, start, end - 1, memo, length))
        return memo[(start, end)]
            
        

```


