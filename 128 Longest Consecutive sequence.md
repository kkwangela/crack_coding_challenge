Imagine you are counting numbers: Given [100, 4, 200, 1, 3, 2], the first number is 100, will you start counting max_length? Yes, because there is no 99, i.e. 100 mush be the start of the consecutive sequence. Continue to look for 101, 102...until you could not find them. Next, you found 4, will you start counting? No, because 3 is in the list, you need to at least start from 3 instead of 4. To make the lookup easier, we can store all numbers in a set or dictionary.
```Python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in d:
                high = num + 1
                while high in d:
                    high += 1 
                res = max(res, high - num)
        return res

```
