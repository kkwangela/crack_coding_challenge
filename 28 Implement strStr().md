## Robin Karp O(M + N)
```Python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or haystack is None: return -1
        m = len(needle)
        n = len(haystack)
        if m == 0: return 0
        if n < m: return -1
        
        base = 10**6
        needleCode = 0
        for i in range(m):
            needleCode = (needleCode * 31 + ord(needle[i])) % base
        
        power = 1
        for i in range(m):
            power = (power * 31) % base
        
        haystackCode = 0
        for i in range(n):
            haystackCode = (haystackCode * 31 + ord(haystack[i])) % base
            if i == m - 1:
                 if haystackCode == needleCode:
                    if needle == haystack[: i + 1]:
                        return 0
            if i >= m:
                haystackCode = (haystackCode - power * ord(haystack[i - m])) % base
                if haystackCode < 0:
                    haystackCode += base
                if haystackCode == needleCode:
                    if needle == haystack[i - m + 1: i + 1]:
                        return i - m + 1
        return -1

```
