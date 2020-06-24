## Method1: Divide and Conquer
Simply divide the lists and merge every two lists.
```Python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        return self.mergeK(0, len(lists) - 1, lists)
    
    def mergeK(self, start, end, lists):
        if start >= end:
            return lists[start]
        
        mid = (start + end) // 2 
        left = self.mergeK(start, mid, lists)
        right = self.mergeK(mid + 1, end, lists)
        return self.merge2Lists(left, right, lists)
    
    def merge2Lists(self, l1, l2, lists):
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                head = head.next 
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next 
        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next
        head.next = None 
        return dummy.next

```
## Heap
Use heap to store k node values, and each time pop the smallest, and then add the next node of the popped node to the heap.
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(h, [l.val, idx])
        dummy = ListNode(0)
        head = dummy
        while h:
            node_val, idx = heapq.heappop(h)
            head.next = ListNode(node_val)
            head = head.next
            if lists[idx].next:
                heapq.heappush(h, [lists[idx].next.val, idx])
                lists[idx] = lists[idx].next
        head.next = None
        return dummy.next
            

```

