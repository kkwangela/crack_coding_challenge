Use a mapping to store node to deep copied node, and traverse all nodes to connect next and random nodes.
```Python

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next 
        
        for node in mapping:
            if node.next:
                mapping[node].next = mapping[node.next]
            if node.random:
                mapping[node].random = mapping[node.random]
        return mapping[head]
        

```
