## Method: BFS
Start by putting all elements in the list to a queue, then pop out to check if it is an integer. If it is, sum += depth * value; else, use getList to store all its elements to queue.

```Python
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        if not nestedList:
            return 0
        
        queue = collections.deque()
        for n in nestedList:
            queue.append(n)
        
        depth = 1 
        res = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.isInteger():
                    res += cur.getInteger() * depth 
                    continue 
                for i in cur.getList():
                    queue.append(i)
            depth += 1 
        
        return res
                

```
