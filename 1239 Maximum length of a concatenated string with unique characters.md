"Maaximum" indicates DP
Travse the list, each time check if it can be added to previously concatinated string. How to check efficiently? Use set and set operations!

```Python
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for s in dp:
                if a & s:
                    continue
                dp.append(a|s)
        return max([(len(a)) for a in dp])

```
