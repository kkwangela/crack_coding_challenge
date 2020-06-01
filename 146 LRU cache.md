Use a modified linked list to store nodes; use a dictionay to store key to previous node so that we can quickly locate the previous node wthout using doubly linked list.
```Python
class LinkedNode:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_prev = {}
        self.capacity = capacity
        self.dummy= LinkedNode(0)
        self.tail = self.dummy
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_prev:
            return -1 
        prev = self.key_to_prev[key]
        curr = prev.next
        self.kick(prev)
        return curr.value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return 
        
        self.push_back(LinkedNode(key, value))
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()
    
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return 
        
        prev.next = node.next
        self.key_to_prev[node.next.key] = prev
        node.next = None
        self.push_back(node)
    
    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        head = self.dummy.next
        self.key_to_prev[head.next.key] = self.dummy
        self.dummy.next = head.next
        del self.key_to_prev[head.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

```
