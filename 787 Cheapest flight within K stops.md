BFS
```Python
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = self.getGraph(n, flights)
        print(graph)
        visited = set()
        visited.add(src)
        queue = collections.deque([(src, 0, K, visited)])
        min_cost = float("inf")
        while queue:
            cur, cost, stop, visited = queue.popleft()
            if cur == dst:
                min_cost = min(min_cost, cost)
            if stop < 0:
                continue
            for neighbor, price in graph[cur]:
                if neighbor in visited:
                    continue
                if cost + price > min_cost:
                    continue
                visited.add(neighbor)
                queue.append((neighbor, cost + price, stop - 1, visited))
                visited.remove(neighbor)
            
        if min_cost == float("inf"):
            return -1 
        return min_cost
        
    def getGraph(self, n, flights):
        graph = {i: [] for i in range(n)}
        for edge in flights:
            start, end, cost = edge[0], edge[1], edge[2]
            graph[start].append((end, cost))
    
        return graph
    
```
