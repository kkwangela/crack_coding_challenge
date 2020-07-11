## Binary Search
```language
[1,2,3,...,P - 1, P, P, P, P + 1, ... , X]
```
Suppose we sort the array. 
Given Y < P, the number of elemetns <= Y is <=Y; and given X >= P, the number of elements >= X is > X.

```Python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        left, right = min(nums), max(nums)
        while left + 1 < right:
            mid = (left + right) // 2 
            if self.smaller_than(nums, mid) <= mid:
                left = mid 
            else:
                right = mid 
        if self.smaller_than(nums, left) > left:
            return left
        return right 
        
    
    def smaller_than(self, nums, mid):
        count = 0
        for n in nums:
            if n <= mid:
                count += 1 
        return count

```


