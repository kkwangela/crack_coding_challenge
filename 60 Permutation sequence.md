The key is to find the number at each position. The idea behind this is to count how many possible permutations there are if starting with, for example 1, and if the number is smaller than k, it means starting with 1 does not satisfy the requirements, then try 2. Until we find the first number, then do the same thing for the second, third, etc.

```Python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i + 1 for i in range(n)]
        for i in range(len(nums)):
            num, kk = self.get_num(nums, k)
            res.append(str(num))
            k = kk 
            nums = [i for i in nums if i != num]
            
        return "".join(res)
    
    def get_num(self, nums, k):
        
        i = 0
        while k > 0 and i < len(nums):
            next_ = self.factorial(len(nums) - 1)
            k -= next_
            i += 1
        
        return nums[i - 1], k + next_
        
        
    def factorial(self, num):
        if num == 1:
            return 1 
        res = 1
        for i in range(1, num + 1):
            res *= i
        return res

```
