The key to this problem is to find two incorrectly placed nodes and exchange their values. How to find them? Suppose we traverse the tree inorderly, and when we first find two consecutive nodes (prev, curr) of wrong order, we find the first incorrectly placed node (prev), and the second incorrectly placed node could be curr, but we need to traverse further to see if there is any other node that have node.val < prev.value. If there is, update the second wrongly place node.
We can do this both iteratively and recursively.
```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = []
        node1, node2 = None, None
        node = root
        while node:
            stack.append(node)
            node = node.left
        
        prev = None
        while stack:
            node = stack[-1]
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            else:
                n = stack.pop()
                while stack and stack[-1].right == n:
                    n = stack.pop()
            
            if prev is not None and prev.val > node.val:
                if node1 is None:
                    node1, node2 = prev, node
                elif node2 is not None:
                    node2 = node 
            prev = node
        
        if node1 is not None:
            node1.val, node2.val = node2.val, node1.val
        return root

```

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.prev = None
        self.node1, self.node2 = None, None
        self.inorder(root)
        if self.node1:
            self.node1.val, self.node2.val = self.node2.val, self.node1.val
        return root
    
    def inorder(self, root):
        if not root:
            return 
        
        self.inorder(root.left)
        if self.prev is not None and self.prev.val > root.val:
            if not self.node1:
                self.node1 = self.prev
                self.node2 = root 
            elif self.node1:
                self.node2 = root 
        self.prev = root
        self.inorder(root.right)
            

```
