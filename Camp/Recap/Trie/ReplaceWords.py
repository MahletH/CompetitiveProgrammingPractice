class Trie:
    def __init__(self):
        self.trie={}
    def insert(self, word: str) -> None:
        head=self.trie
        for char in word:
            if char in head:
                head=head[char]
            else:
                head[char]={}
                head=head[char]
        head['#']=True
    def search(self, word: str) -> bool:
        new_word=[]
        head=self.trie
        for char in word:
            if '#' in head:
                return "".join(new_word)
            elif char in head:
                new_word.append(char)
                head=head[char]
            else:
                return word
        if '#' in head:
            return "".join(new_word)
        else:
            return word
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
        res=[]
        sentence=sentence.split(" ")
        for word in sentence:
            res.append(trie.search(word))
        return " ".join(res)