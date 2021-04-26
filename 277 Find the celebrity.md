two pass
Fristly find a candidate. How? By traverse through the list, every time we compare if the candidate knows x, if it dose, then candidate becomes x.
After traversal, we need to check if the candidate is really a celebrity. How? Make sure it is known by each other person, and if does not know any other person.
```Python
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        for i in range(n):
            if i != candidate and knows(i, candidate) == 0:
                return -1
            if i != candidate and knows(candidate, i) == 1:
                return -1
    
        return candidate

```
