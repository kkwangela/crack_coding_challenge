## Method1: O(N^2)
dp[i] = longest subsequence ending at nums[i]
prev[i]: the index of the previous node of the longest subsequence
```Python

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1 for _ in range(len(nums))]
        prev = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        longest = max(dp)
        last = dp.index(longest)
        path = []
        while last != -1:
            path.append(last)
            last = prev[last]
        path = path[::-1]
        return max(dp)
```
## Method2: O(NlogN)
dp[i] = the smallest number of the subsequnce of length i.
Use binary search to find the position to insert nums[i], and then update dp[index].
```Python
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums) + 1)]
        dp[1] = nums[0]
        max_len = 1
        for i in range(1, len(nums)):
            if nums[i] > dp[max_len]:
                max_len += 1 
                dp[max_len] = nums[i]
            else:
                #index = bisect.bisect_left(dp, nums[i], 1, max_len)
                #dp[index] = min(dp[index], nums[i])
                #[0, 1, 3, 5, 7], 插入6
                #             ^ 这才是想要return的值，dp[index] > nums[i]
                left, right = 1, max_len
                while left + 1 < right:
                    mid = (left + right) // 2 
                    if dp[mid] >= nums[i]:
                        right = mid 
                    else:
                        left = mid 
                if dp[left] < nums[i]:
                    dp[right] = min(dp[right], nums[i])
                else:
                    dp[left] = min(dp[left], nums[i])
                
        return max_len

```

