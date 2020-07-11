```Python
from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heappush(heap, [heightMap[i][j], i, j])
                    visited.add((i, j))
        res = 0
        while heap:
            cur, x, y = heappop(heap)
            for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if (nx, ny) in visited:
                    continue
                next_height = max(heightMap[nx][ny], cur)
                res += next_height - heightMap[nx][ny]
                visited.add((nx, ny))
                heappush(heap, [next_height, nx, ny])
        return res

```
