DFS. Start by calculating the number of left and right parenthesis in the string. A trick is to calculate the relative number instead of actual number. e.g. () would be counted as left = 0 and right = 0; )( is counted as left = 1 and right = 1. 
Although the problem asks us to remove the minimum number of parenthesis, we do not actually need to get the 
"minimum number"; instead, once we found a valid string, we stop continue to look for removing other parenthesis.

```Python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = self.count(s)
        res = []
        self.dfs(s, left, right, 0, res)
        if len(res) == 0:
            res.append("")
        return res
        
    def dfs(self, s, left, right, start, res):
        if left == right == 0:
            if self.isValid(s):
                res.append(s)
                return
        
        for i in range(start, len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            if s[i] == "(" and left > 0:
                self.dfs(s[:i] + s[i + 1:], left - 1, right, i, res)
            if s[i] == ")" and right > 0:
                self.dfs(s[:i] + s[i + 1:], left, right - 1, i, res)
               
        
    def count(self, s):
        #这种count方式考虑到了右括号在左括号前面的情况：)(: left = 1, right = 1; ():left = right = 0
        left, right = 0, 0
        for c in s:
            if c == "(":
                left += 1 
            elif c == ")":
                if left > 0:
                    left -= 1 
                else:
                    right += 1 
        return left, right
    
    def isValid(self, s):
        left, right = self.count(s)
        return left == 0 and right == 0
            

```
