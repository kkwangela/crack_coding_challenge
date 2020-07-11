Start from the lower left corner. Each time compare if with the target: if it is smaller than the target, then the column is ruled out; if it is bigger, then the row is ruled out.
```Python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col <n:
            if matrix[row][col] < target:
                col += 1 
            elif matrix[row][col] > target:
                row -= 1 
 
            else:
                return True
        return False

```
