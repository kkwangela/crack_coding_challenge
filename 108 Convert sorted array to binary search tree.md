Start by finding the root of the tree: the middle number of the array. Then, iteratively look for its left and right child by checking the middle number of the left/right part of the array.
```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left =self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

```
