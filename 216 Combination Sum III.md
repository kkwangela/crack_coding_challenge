## DFS
```Python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = list(range(1, 10))
        visited = set()
        self.dfs(k, n, [], visited, nums, res)
        return res
    
    def dfs(self, k, n, path, visited, nums, res):
        if k == 0:
            if sum(path) == n:
                res.append(path[:])
            return 
        
        for i in nums:
            if i in visited:
                continue
            if path and i <= path[-1]:
                continue
            if sum(path) + i > n:
                continue
            visited.add(i)
            self.dfs(k - 1, n, path + [i], visited, nums, res)
            visited.remove(i)

```
## BFS
```Python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        start = [[i] for i in range(1, min(10, n + 1))]
        queue = collections.deque(start)
        
        res = []
        while queue:
            cur = queue.popleft()
            
            if len(cur) == k and sum(cur) == n:
                res.append(cur)
            if len(cur) >= k:
                continue
            for num in nums:
                if num <= cur[-1]:
                    continue
                if num + sum(cur) > n:
                    continue
                queue.append(cur + [num])
        return res
            

```
