 ## Prefix + dict
Frist calculate prefix sum by scanning all numbers and check if
```Python
prefix - k
```
is in the dictionary. If it is, calculate the length of the subarry; otherwise, if the number of current prefix sum if not existed, add it into the dict. Do not replace those visited prefix sum as we only want to know the first index that it appears.
```Python
    def maxSubArrayLen(self, nums, k):
        d = {0: -1}
        prefix = 0
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in d:
                res = max(res, i - d[prefix - k])
            else:
                if prefix not in d:
                    d[prefix] = i 
        return res

```

