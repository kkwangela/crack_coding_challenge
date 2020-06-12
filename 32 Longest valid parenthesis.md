## Mthod1: stack
Every time we find ")", we will need to update the max_length by checking current index  - index of one before corresponding 
"(".

```Python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res

```
## Method2: DP
dp[i] = length of invalid substring frm i to the end of s
dp[i] = 0 for s[i] = ")". When s[i] = "(", first we need to look for ")", by looking at index i + dp[i + 1] + 1. Here dp[i + 1] is for the case of () inside of a larger (), and if s[i + 1] = ), it will not affect the result since dp[i + 1] will be 0. Secondly, we need to add the length starting from index i + dp[i + 1] + 2.
```Python
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        if not s:return 0
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == ")":
                if i > 0 and s[i-1] == "(":
                #找到了对应的（，加上（之前的数字（可能是0， 可能大于0）
                    dp[i] = dp[i-2] + 2
                elif i > 0 and s[i-1] == ")":
                    if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == "(":
                        dp[i] = 2 + dp[i-1] + dp[i - dp[i-1] -2]
        return max(dp)
        """
        #dp倒着来，dp[i]表示i开头到结尾有多长的valid parenthesis
        #所有")"对应的dp都是0.每遇到一个（，首先要找其对应的“）”，然后加上对应的）后一位的dp
        if not s: return 0
        dp = [0 for _ in range(len(s))]
        res = 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "(":
                if i + dp[i + 1] + 1 < len(s) and s[i + dp[i + 1] + 1] == ")":
                    dp[i] = 2 + dp[i + 1]
                    if i + dp[i + 1] + 2 < len(s):
                        dp[i] += dp[i + dp[i + 1] + 2]
                res = max(res, dp[i])
        return res
        

```
