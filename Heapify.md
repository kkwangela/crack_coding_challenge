There are two methods to heapify an array: sift up and sift down. Given an index k, the index of the father of this node is **(k - 1) // 2**; the index of the son of this node is **k * 2 + 1** and **k * 2 + 2**.

**Sift Up**: for each element in array, compare it with its fater node if it is smaller than its fater node, exchange them. Continue until the node is lager than its fater.

**Sift down**: Start by choose the father node that is closest to leaves, compare it with its two sons. If it is larger than the smaller son, exchange them. Continue unitl it has no further son.
```Python
    def heapify(self, A):
        #for i in range(len(A) - 1, -1, -1):
         #   self.siftDown(A, i)
        for i in range(len(A)):
            self.siftUp(A, i)
    
    def siftDown(self, A, k):
        while k * 2 + 1 < len(A):
            son = k * 2 + 1
            if k * 2 + 2 < len(A) and A[son] > A[k * 2 + 2]:
                son = k * 2 + 2 #check if right son is smaller than left son; choose the smaller one
            if A[son] >= A[k]:
                break #means this node is done
            #father node is bigger than son. exchage
            A[son], A[k] = A[k], A[son]
            k = son 
            
    
    
    def siftUp(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father

```
