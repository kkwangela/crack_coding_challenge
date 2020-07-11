## Stack O(N)
```Python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        data = path.split("/")
        for d in data:
            if d == "..":
                if stack:
                    stack.pop()
            elif d == "" or d == "." or d == "/":
                continue 
            else:
                stack.append(d)
        print(stack)
        if stack:
            res = "/".join(stack)
            return "/" + res
        return "/"

```
