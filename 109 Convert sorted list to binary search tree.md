Same idea with 108. Instead, we need to find the middle node a linked list. One thing to notice is that when we find the middle node, we need to cut it from its previous node to avoid infinite loop. 
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None 
        slow, fast = head, head.next
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        new_head = slow.next
        root = TreeNode(slow.val)
        #把中点和前面的node砍断
        if prev:
            prev.next = None
        else: #说明slow就是中点，所以head左边没有值了，把head设置为None
            head = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(new_head)
        
        return root
            

```
