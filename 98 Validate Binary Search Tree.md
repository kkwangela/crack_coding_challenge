## Divide and Conquer
Current node is bigger than the biggest value of its  left children, smaller than the smallest of its right children.
```Python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        isValid, _, _ = self.dfs(root)
        return isValid
        
    def dfs(self, root):
        if not root:
            return True, -float("inf"), float("inf")
        left, left_max, left_min = self.dfs(root.left)
        right, right_max, right_min = self.dfs(root.right)
        if not left or not right:
            return False, 0, 0
        
        if root.val > left_max and root.val < right_min:
            return True, max(left_max, right_max, root.val), min(left_min, right_min, root.val)
        return False, 0, 0

```
## DFS
Current node must satisfy some conditions and its left and right children also have to satisfies certain conditions.
```Python
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        return self.dfs(root, -float("inf"), float("inf"))
        
    def dfs(self, root, sub_max, sub_min):
        if not root:
            return True
        if root.val <= sub_max or root.val >= sub_min:
            return False
        return self.dfs(root.left, sub_max, min(sub_min, root.val)) and self.dfs(root.right, max(sub_max, root.val), sub_min)

```
