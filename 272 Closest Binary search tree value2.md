Firstly, we look for the closest node to target. Then, use BST iterator to find subsequent closest numbers.
```Python
    def closestKValues(self, root, target, k):
        res = []
        lower_stack = self.get_stack(root, target)
        upper_stack = list(lower_stack)
        if lower_stack[-1].val < target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)
        #print(lower_stack[-1].val)
        #print(upper_stack[-1].val)
        for i in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                res.append(lower_stack[-1].val)
                #print(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                res.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
        
        return res 
    
    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return stack
    
    def move_upper(self, stack):
        #find next root (inorder)
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
    
    def move_lower(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
    
    def is_lower_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False 
        if not upper_stack:
            return True
            
        if (upper_stack[-1].val - target > target - lower_stack[-1].val):
            return True
        return False
    

```
