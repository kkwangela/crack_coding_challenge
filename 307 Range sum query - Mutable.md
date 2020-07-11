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
    def build(self, start, end, nums):
        if start > end:
            return None
        if start == end:
            return segmentTree(start, end, nums[start])
        root = segmentTree(start, end, nums[start])
        mid = (start + end) // 2
        root.left = self.build(start, mid, nums)
        root.right = self.build(mid + 1, end, nums)
        if root.left and root.right:
            root.val = root.left.val + root.right.val
        return root
    
    def modify(self, root, index, val):
        if root.start == root.end:
            root.val = val
            return 
        mid = (root.start + root.end) // 2 
        if index <= mid:
            self.modify(root.left, index, val)
        else:
            self.modify(root.right, index, val)
        root.val = root.left.val + root.right.val
        return
    
    def query(self, root, start, end):
        if not root:
            return 0
        if root.start == start and root.end == end:
            return root.val
        if start > end:
            return 0
        mid = (root.start + root.end) // 2
        if end > mid:
            if start <= mid:
                left = self.query(root.left, start, mid)
                right = self.query(root.right, mid + 1, end)
                return left + right
            else:
                return self.query(root.right, start, end)
        else:
            return self.query(root.left, start, end)
            
    
    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return None
        self.root = self.build(0, len(nums) - 1, nums)

    def update(self, i: int, val: int) -> None:
        self.modify(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.query(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

```

