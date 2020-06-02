Method1: prefix sum
Method2: Segment tree

```Python
class segmentTree:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left, self.right = None, None
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        if len(nums) == 0:
            return None 
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, start, end):
        root = segmentTree(start, end, nums[start])
        if start >= end:
            return root 
        mid = (start + end) // 2
        root.left = self.build(nums, start, mid)
        root.right = self.build(nums, mid + 1, end)
        if root.left and root.right:
            root.val = root.left.val + root.right.val 
            
        return root
        
    def modify(self, root,  index, val):
        if root.start == root.end:
            root.val = val 
            return
        if root is None:
            return
        mid = (root.start + root.end) // 2 
        if index <= mid:
            self.modify(root.left, index, val)
        else:
            self.modify(root.right, index, val)

        root.val = root.left.val + root.right.val
        return 
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.modify(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
       
        return self.query(self.root, i, j)
        
    def query(self, root, start, end):
        if start > end:
            return 0 
        if root.start >= start and root.end <= end:
            return root.val 
        if start > root.end or end < root.start:
            return 0
        return self.query(root.left, start, end) + self.query(root.right, start, end)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

```

