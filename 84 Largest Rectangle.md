## Monotonic stack
The largest area at each point = height at that point * (first smaller point right to current, first smaller point left to current).
```Python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        heights.append(-1)
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0 
                right = i - 1 
                area = (right - left + 1) * h 
                res = max(res, area)
        
            stack.append(i)
        
        return res
        

```
