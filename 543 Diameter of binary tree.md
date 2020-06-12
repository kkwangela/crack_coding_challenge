Divide and Conquer.
Suppose we know the height of left and right child, then the max_len at this point is left + right + 1 - 1 (starting from left, walk through current root, then go to right child). Also, the height of current root is max(left, right) + 1.
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_len = 0
        longest = self.dfs(root)
        return self.max_len
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        self.max_len = max(self.max_len, left + right)
        return max(left, right) + 1

```
