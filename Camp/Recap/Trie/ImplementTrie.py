class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie={}
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head=self.trie
        for char in word:
            if char in head:
                head=head[char]
            else:
                head[char]={}
                head=head[char]
        head['#']=True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        head=self.trie
        for char in word:
            if char in head:
                head=head[char]
            else:
                return False
        return '#' in head

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head=self.trie
        for char in prefix:
            if char in head:
                head=head[char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)