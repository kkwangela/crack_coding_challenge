Classic backtracking(DFS) problem. Consider it as putting four "." in the string and record the valid IP address.
Notice that each section in the IP address must be in the range [0, 255]. And be careful for the case "012" becase if we directly convert using int function, it will neglect the first "0".

```Python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, 0, [], res)
        return res 
    
    def dfs(self, s, index, dot, path, res):
        if dot == 4:
            if index == len(s):
                res.append(".".join(path))
            return 
        
        for j in range(index + 1, index + 4):
            if j > len(s):
                continue
            tmp = s[index: j]
            if j > index + 1 and tmp[0] == "0":
                continue 
            if int(tmp) >= 0 and int(tmp) <= 255:
                self.dfs(s, j, dot + 1, path + [tmp], res)

```
