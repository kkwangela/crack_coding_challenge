## Binary search
The more parts we divide the array, the smaller the maximum of each parts will be. So the key is to find the smallest maximum value that within m parts.
```Python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #二分答案法
        if not nums:
            return 0
        left, right = max(nums), sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2 
            if self.num_of_parts(nums, mid) <= m:
                right = mid 
            else:
                left = mid 
            
        if self.num_of_parts(nums, left) <= m:
            return left 
        return right 
    
    def num_of_parts(self, nums, value):
        #calculate the number of parrts needed to have min max(subarray) = value
        cur = 0
        parts = 1
        for num in nums:
            if cur + num > value:
                cur = num
                parts += 1 
            else:
                cur += num
        return parts

```

