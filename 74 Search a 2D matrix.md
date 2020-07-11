If we expand the matrix row by row, it becomes a one-D sorted array. To find the target, we can use binary search. 
## Convert 1D index to 2D coords:
x = index // col; y = index % col

```Python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #如果一行一行读下来的话，是一个一维的递增array。用二分法
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            #to get the coords, divide by the number of column
            x, y = mid // n, mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                right = mid 
            else:
                left = mid
        
        #print(left, right)
        x, y = left // n, left % n
        if matrix[x][y] == target:
            return True
        x, y = right // n, right % n
        
        if matrix[x][y] == target:
            return True
        return False

```
