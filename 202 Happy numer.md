Use hashset to record the numbers that have appeared. If it reappears, return False

```Python
class Solution:
    def isHappy(self, n: int) -> bool:
        #if a repeated number appears, it is not a happy number
        visited = set()
        visited.add(n)
        n = str(n)
        while True:
            n = [int(i) ** 2 for i in n]
            n = sum(n)
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            n = str(n)

```
