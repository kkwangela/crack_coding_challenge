Divide and Conquer
```Python

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        max_path, _ = self.divideConquer(root)
        return max_path
    
    def divideConquer(self, root):
        if not root:
            return -float("inf"), 0
            
        left_max, left = self.divideConquer(root.left)
        right_max, right = self.divideConquer(root.right)
        
        max_path = max(left_max, right_max, left + right + root.val)
        current = max(left + root.val, right + root.val, 0)
        return max_path, current


```
