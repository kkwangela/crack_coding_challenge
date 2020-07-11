The core of this problem is to traverse a binary tree. So obvusly, we can do it by ++bfs or dfs.++
## BFS
```Python
def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = collections.deque([(root, root.val)])
        while queue:
            node, val = queue.popleft()
            if node.left == None and node.right == None:
                res += val
            if node.left:
                queue.append((node.left, val * 10 + node.left.val))
            if node.right:
                queue.append((node.right, val * 10 + node.right.val))
        return res

```
## DFS
```Python
def sumNumbers(self, root: TreeNode) -> int:
        
        return self.dfs(root, 0)
    
    def dfs(self, root, prev):
        if root == None:
            return 0
        
        cur = prev * 10 + root.val
        if root.left == None and root.right == None:
            return cur
        
        return self.dfs(root.left, cur) + self.dfs(root.right, cur)

```


