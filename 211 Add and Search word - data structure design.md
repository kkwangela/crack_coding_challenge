## Trie + DFS
```Python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root = self.root
        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
        root.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        return self.dfs(root, 0, word)

    def dfs(self, root, index, word):
        if index >= len(word):
            if root.isWord:
                return  True
            return False
        
        if word[index] != ".":
            root = root.children.get(word[index], None)
            if root == None:
                return False
            return self.dfs(root, index + 1, word)
        else:
            for c in root.children:
                if self.dfs(root.children[c], index + 1, word):
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

```
