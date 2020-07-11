## Prefix sum + dict O(N), O(N)
```Python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        prefix_dict = {0: 1}
        res = 0
        
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in prefix_dict:
                res += prefix_dict[prefix - k]
            if prefix in prefix_dict:
                prefix_dict[prefix] += 1 
            else:
                prefix_dict[prefix] = 1 
        return res

```
