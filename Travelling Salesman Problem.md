The problem is to get the smallest cost to travel each point exactly once.
DFS can obviously solve the question, but we need to improve it.
## Method1: DFS with prunning
First, we use a **get_graph** function to get the neighbors of each node and the cost between them.
Then we need a **has_better_path** function to do prunning. What does this function do? Consider we have a path: [1,2,3,4,5], and the next city we will visit is 6. If we exchange 2 and 5, then the path would be [1,5,3,4,2]. We can compare the cost 1 to 2 + 5 to 6 with the cost 1 to 5 + 2 to 6, if the latter is smaller, that we do not need to further consider this [1,2,3,4,5] option since it is definately not the minimum cost. Similarly, if exchaning 1, 5 does not result in a better path, exchange 5 with 3 and 4 and see if there is a better solution. If there is, we can skip this path.
**Next question is**: Why do you only consider exchanging the last city in the path with others? Why not try every pair? Becase when you reach for example city 4, and the path is [1,2,3,4], you'd have already tried exchanging 4 with 2 and 3.

```Python
class Result:
    def __init__(self):
        self.res = float("inf")
        
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        graph = self.get_graph(n, roads)
        result = Result()
        visited = set()
        visited.add(1)
        self.dfs(graph, 1, 0, [1], visited, result)
        return result.res
        
    def dfs(self, graph, cur, cost, path, visited, result):
        if len(visited) == len(graph):
            result.res = min(result.res, cost)
            return 
        
        for city in graph[cur]:
            if city in visited:
                continue 
            if self.has_better_path(graph, path, city):
                continue 
            visited.add(city)
            path.append(city)
            self.dfs(graph, city, cost + graph[cur][city], path, visited, result)
            visited.remove(city)
            path.pop()
            
    def get_graph(self, n, roads):
        graph = {i: {j: float("inf") for j in range(1, n + 1) if j != i} for i in range(1, n + 1)}
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph
            
    def has_better_path(self, graph, path, city):
        for i in range(1, len(path)):
            if graph[path[i - 1]][path[i]] + graph[path[-1]][city] > \
            graph[path[i]][city] + graph[path[-1]][path[i - 1]]:
                return True 
        return False
```


