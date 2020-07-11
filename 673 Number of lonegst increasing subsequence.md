Similar to LIS. This time, we need another list count, and count[i] = the number of subsequence at index[i] with length dp[i]

When nums[i] > nums[j]:
Two cases o consider:
1) dp[j] + 1 < dp[i]:
It means dp[i] will be updated, and correspondingly, count[i] = count[j] because we simply add one value to subsequences at index j, and no more subsequence is added;
2) dp[j] + 1 == dp[i]:
dp[i] need not to be updated. Subsequences at index[j] can be extended by add one elemenet nums[i] to thier end, so count[i] will also add count[j] elements.
```Python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        count = [1] * len(nums)
        longest = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue 
                if dp[j] + 1 == dp[i]: #说明nums[j]跟在nums[i]后面符合条件，不会影响longest
                    count[i] += count[j] #在dp[i]条件下，j对应的都符合，所以要把j对应的加进来
                if dp[j] + 1 > dp[i]: #说明longest要更新，则此时对应的count和j对应的count相同
                    dp[i] = dp[j] + 1
                    longest = max(longest, dp[i])
                    count[i] = count[j] #现在的count应该就是j对应的count，只是把对应的list都加了一个数
        res = 0
        for i in range(len(nums)):
            if dp[i] == longest:
                res += count[i]
        return res
                

```
