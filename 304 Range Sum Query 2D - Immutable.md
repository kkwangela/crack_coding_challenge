Use prefix-sum to record the sum of the matrix from [0, 0] to [i, j]. Also, use column_sum to keep track of the sum of each column from row 0 to row i, so that we do not need to check all elements above row i.
```Python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        col_sum = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                col_sum[j] += matrix[i - 1][j - 1]
                self.prefix_sum[i][j] = self.prefix_sum[i][j - 1] + col_sum[j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2 + 1][col2 + 1] + self.prefix_sum[row1][col1] - self.prefix_sum[row2 + 1][col1] - self.prefix_sum[row1][col2 + 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

```

