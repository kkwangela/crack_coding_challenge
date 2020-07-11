## Monotonic stack
```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        nums.append(float("inf"))
        treenode = [TreeNode(n) for n in nums]
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                node = treenode[stack.pop()]
                left = nums[stack[-1]] if stack else float("inf")
                if left < nums[i]:
                    treenode[stack[-1]].right = node
                else:
                    treenode[i].left = node
            stack.append(i)
        
        return treenode[-1].left

```
