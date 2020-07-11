## Binary search + Robon Karp O(NlogN)
```Python
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        if not S:
            return ""
        ans = ""
        left, right = 0, len(S)
        while left + 1 < right:
            #print(left, right)
            mid = (left + right) // 2 
            found, sub = self.is_duplicate(S, mid)
            if found:
                ans = sub
                left = mid
            else:
                right = mid 
                
        
        found, sub = self.is_duplicate(S, right)
        if found:
            return sub
        found, sub = self.is_duplicate(S, left)
        if found :
            return sub
        
        return ans
    
    def is_duplicate(self, S, length):
        base = 10 ** 6
        cur = 0
        vis = collections.defaultdict(list)
        power = 1
        for i in range(length):
            power = (power * 31) % base
            
        for i in range(len(S)):
            cur = (cur * 31 + (ord(S[i]) - ord("a"))) % base
            if i == length - 1:
                vis[cur].append(i)
            
            if i > length - 1:
                cur = (cur - (ord(S[i - length]) - ord("a")) * power) % base
                if cur < 0:
                    cur += base
                if cur in vis:
                    for index in vis[cur]:
                        if S[index - length + 1: index + 1] == S[i - length + 1: i + 1]:
                            return True, S[i - length + 1: i + 1]
                vis[cur].append(i)
        
        return False, ""

```
