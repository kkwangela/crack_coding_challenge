## Method1: DFS with memoization
Record the number of words each word uses to concatenate; Pay attention to the case of "".

```Python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words:
            return []
        word_set = set([word for word in words if len(word) >= 1])
        min_len = min([len(w) for w in words])
        res = []
        memo = {}
        
        for word in words:
            if len(word) <= min_len:
                continue
            if self.dfs(word, 0, min_len, word_set, 0, memo):
                res.append(word)
        return res
    
    def dfs(self, word, start, min_len, word_set, num, memo):
        if start >= len(word) and num >= 2:
            return True
        if word[start:] in word_set and num + 1 >= 2:
            return True
        if word[start:] in memo:
            return memo[word[start:]]
        
        memo[word[start:]] = False
        for i in range(start + 1, len(word) + 1):
            prefix = word[start: i]
            if prefix in word_set:
                #print(prefix, word[i:])
                if self.dfs(word, i, min_len, word_set, num + 1, memo):
                    memo[word[start:]] = True
                    return True
        return False

```

## DP
Similar to word break. The difference is each word has to be concatenated by >= 2 words. So candicate word set has to remove the word itself if it is a candidate word.
```Python
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        word_set = set(words)
        for word in words:
            word_set.remove(word)
            if self.wordBreak(word, word_set):
                res.append(word)
            word_set.add(word)
        
        return res 
    
    def wordBreak(self, word, word_set):
        if not word:
            return False
        dp = [False for _ in range(len(word) + 1)]
        dp[0] = True
        for i in range(1, len(word) + 1):
            for j in range(i):
                if dp[j] and word[j: i] in word_set:
                    dp[i] = True
                    break 
        return dp[-1]
        

```

