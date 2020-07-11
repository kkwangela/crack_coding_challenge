## DFS
One special case to notice: It is not guaranteed that using an offer will be cheaper. A case would be all prices are 0 but offers cost more than 0.

```Python
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.dfs(price, special, needs, 0)
    
    def dfs(self, price, special, needs, cost):
        if sum(needs) == 0:
            return cost
        
        min_cost = float("inf")
        for s in special:
            if not self.is_valid_special(s, needs):
                continue
            next_needs = []
            for i in range(len(needs)):
                next_needs.append(needs[i] - s[i])
            next_cost = cost + s[-1]
            min_cost = min(min_cost, self.dfs(price, special, next_needs, next_cost))
#compare with not using any offer        
        min_cost = min(min_cost, cost + sum([price[i] * needs[i] for i in range(len(needs))]))
        
        return min_cost
    
    def is_valid_special(self, s, needs):
        for i in range(len(needs)):
            if s[i] > needs[i]:
                return False
        return True

```
