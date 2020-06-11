It is similar to quick sort. Now the pivot is 1. 
```Python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        left, right = 0, len(nums) - 1 
        while i <= right:
            if nums[i] == 1:
                i += 1 
            
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                
            else:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
                
```
