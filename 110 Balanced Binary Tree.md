Divide and Conquer. If it is knonwn that the depth of the right child and left child of a node, we can easily see if it is balanced at that node. At the same  time, keep track of the current depth: max(left, right) + 1 to pass upward.
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _, isBalanced = self.dfs(root)
        return isBalanced
    
    def dfs(self, root):
        if not root:
            return 0, True
        left, b1 = self.dfs(root.left)
        right, b2 = self.dfs(root.right)
        
        return max(left, right) + 1, b1 and b2 and abs(left - right) <= 1
    

```
