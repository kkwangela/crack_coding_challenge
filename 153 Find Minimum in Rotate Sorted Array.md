## Binary search
There are two cases: minimum is on the left of mid and on the right of mid. We need to figure out which case it is. The answer is to compare is with the last number in the array. It will be problematic if you compare it with the first element, and the counter exmple is a sorted array without rotation.

```Python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid] >= nums[-1]:
                if nums[mid] < nums[mid + 1]:
                    left = mid
                else:
                    return nums[mid + 1]
            else:
                if nums[mid] < nums[mid + 1]:
                    right = mid
                else:
                    return nums[mid + 1]
        #print(left, right)
        if nums[left] < nums[right]:
            return nums[left]
        return nums[right]

```
