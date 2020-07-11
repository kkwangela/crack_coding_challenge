## Monotonic stack
Similar to 84. Consider row[0] to row[i] as a histogram and calculate the height of each point.
```Python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        heights = [0 for _ in range(len(matrix[0]))]
        heights.append(-1)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[j] += 1 
                else:
                    heights[j] = 0
            
            stack = []
            for j in range(len(heights)):
                while stack and heights[stack[-1]] >= heights[j]:
                    h = heights[stack.pop()]
                    left = stack[-1] + 1 if stack else 0 
                    right = j - 1 
                    area = (right - left + 1) * h
                    res = max(res, area)
                stack.append(j)
        return res

```
