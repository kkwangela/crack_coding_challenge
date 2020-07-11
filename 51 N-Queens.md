Classic DFS. The condition for a valid position is: the next chess is not in the same col of previous chess and r + c != row + col ans r - c != row - col for all determined r and c.
```Python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0:
            return []
        self.dfs(n, 0, [], res)
        return res
    
    def dfs(self, n, row, cols, res):
        if n == row:
            board = self.draw(cols)
            res.append(board)
            return
        
        for i in range(n):
            if not self.isValid(n, row, cols, i):
                continue
            cols.append(i)
            self.dfs(n, row + 1, cols, res)
            cols.pop()
            
            
    def isValid(self, n, row, cols, i):
        for r, c in enumerate(cols):
            if c == i:
                return False
            if r - c == row - i or r + c == row + i:
                return False      
        return True
    
    def draw(self, cols):
        n = len(cols)
        board = []
        
        for i in range(n):
            strs = ["."] * n
            strs[cols[i]] = "Q"
            board.append("".join(strs))
        return board

```
