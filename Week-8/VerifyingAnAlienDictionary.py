class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Just a reminder that you're an amazing human being
        # Keep being awesome
        alien_dict={}
        for i,character in enumerate(order):
            alien_dict[character]=i
        for i in range(1,len(words)):
            word1,word2=words[i-1],words[i]
            for j in range(len(word1)):
                if j==len(word2):
                    return False
                if alien_dict[word1[j]]<alien_dict[word2[j]]:
                    break
                elif alien_dict[word1[j]]>alien_dict[word2[j]]:
                    return False
        return True