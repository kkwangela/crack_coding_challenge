Connect the end of the first Linked list to the head of the second linked list, and now the problem becomes: find the starting node of the circle in the linked list. At the end, restore the original linked list.
```Python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        node = headA
        while node and node.next:
            node = node.next
        node.next = headB
        
        slow, fast = headA, headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = headA
                break
        if fast != headA:
            node.next = None
            return None 
        
        while fast != slow:
            slow = slow.next
            fast = fast.next
        node.next = None
        return slow

```
