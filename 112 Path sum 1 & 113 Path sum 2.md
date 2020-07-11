Divide and Conquer
Usually, when we use divide and conquner method to solve tree-related problem, we simply thorow its left and right child to DFS funtion. However, in this problem, since we have to guarantee the path is from root to a leave, we must check if the node is a leaf node. Otherwise, we cannot pass the test case: [1,2], target = 1.
### Path Sum I
```Python
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        return self.dfs(root, target)
    
    def dfs(self, root, target):
        if not root:
            return False
        if root.val == target and not root.left and not root.right:
            return True
        else:
            return self.dfs(root.left, target - root.val) or self.dfs(root.right, target - root.val)
```
### Path Sum II
```Python
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        self.dfs(root, target, res, [])
        return res
        
    def dfs(self, root, target, res, path):
        if not root:
            return
        if root.val == target and root.left == None and root.right == None:
            res.append(path[:] + [root.val])
        else:
            return self.dfs(root.left, target - root.val, res, path + [root.val]) or \
            self.dfs(root.right, target - root.val, res, path + [root.val])

```


