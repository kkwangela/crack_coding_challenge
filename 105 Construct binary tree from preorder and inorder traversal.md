The first element of preorder is the root. Find the index of root in inorder array, the laft part are left children of the root and right part are the right children. Notice that to find the next left/right node, since we first go left, we only need to pop the first element of the preorder array to get the node; and the rest will go to the right node.
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if not inorder:
            return None
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root 

```
