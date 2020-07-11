## Prefix sum + dict
```Python
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 0
        prefix_hash = {0: -1}
        res = -float("inf")
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix += 1 
            else:
                prefix -= 1 
            
            if prefix in prefix_hash:
                res = max(res, i - prefix_hash[prefix])
            else:
                prefix_hash[prefix] = i 
        return res if res != -float("inf") else 0

```
