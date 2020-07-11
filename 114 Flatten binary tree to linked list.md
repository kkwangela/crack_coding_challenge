Divide and Conquer
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        #怎么可能return left和right呢？他们就是root.left, root.right
        #应该return left_last，right_last
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)
        #connect
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        return right_last or left_last or root

```

