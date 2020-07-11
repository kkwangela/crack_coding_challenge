Divide and Conquer
```Python
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        self.average = -float("inf")
        self.root = root
        
        self.divideConquer(root)
        return self.root
    
    def divideConquer(self, root):
        if not root:
            return 0, 0
        
        left, size1 = self.divideConquer(root.left)
        right, size2 = self.divideConquer(root.right)
        
        size = size1 + size2 + 1
        total = left + right + root.val
        cur = total / size 
        if cur > self.average:
            self.average = cur
            self.root = root 
        
        return total, size

```
