Divide and Conquer \n
Suppose the left anf riht child of a node has been inverted, what do we do with the current node? We interchange its left and right nodes.
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root = self.divideConquer(root)
        return root
    
    def divideConquer(self, root):
        if not root:
            return None
        left = self.divideConquer(root.left)
        right = self.divideConquer(root.right)
        
        if left and right:
            root.right = left
            root.left = right
        elif left:
            root.right = left
            root.left = None
        elif right:
            root.left = right
            root.right = None
        return root

```
