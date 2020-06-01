Since this question did not ask to edit in-place, we can **create two linked-lists**: one store nodes smaller than x in order and the other one stores nodes larger than x in order.
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        l1, l2 = ListNode(0), ListNode(0)
        dummy1 = l1
        dummy2 = l2
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l1.next = dummy2.next 
        l2.next = None
        return dummy1.next


```
