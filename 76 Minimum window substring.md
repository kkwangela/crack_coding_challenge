## Two pointers
diff = how many of the characters in target are not matched by source; count = the frequency of each character in target, vis = the frequency of each character in source from i to j.
```Python
    def minWindow(self, source , target):
        if not target or not source:
            return ""
        vis = {}
        j = 0
        res = ""
        count = collections.Counter(target)
        diff = len(count)
        for i in range(len(source)):
            while j < len(source) and diff > 0:
                vis[source[j]] = vis.get(source[j], 0) + 1 
                if source[j] in count and vis[source[j]] == count[source[j]]:
                    diff -= 1 
                j += 1 
            if diff == 0:
                
                if res == "" or j - i < len(res):
                    res = source[i:j]

            #print(vis)
            if source[i] in count and vis[source[i]] == count[source[i]]:
                diff += 1 
            vis[source[i]] -= 1 
        return res
                

```
