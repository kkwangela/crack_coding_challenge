Use two pointers as a sliding window.
```Python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        res = float("inf")
        tmp_sum = nums[0]
        j = 1
        for i in range(len(nums)):
            j = max(j, i + 1)
            while j < len(nums) and tmp_sum < s:
                tmp_sum += nums[j]
                j += 1 
            #跳出这个循环的条件是tmp_sum >= s或者j = len(nums)
            if tmp_sum >= s: #用于应对j = len(nums)的情况，i可以继续往右
                res = min(res, j - i)
                tmp_sum -= nums[i]
            else:
                break

        if res == float("inf"): res = 0
        return res

```
