Scan all grid for "1", and once we find a "1", firstly add 4 to answer, then check its right and down neighbors(or left and upper), each neighbor "1" will cost reuction of 2 to the answer.
```Python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 4 
                    for dx, dy in [[1, 0], [0, 1]]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            ans -= 2 
        return ans

```
