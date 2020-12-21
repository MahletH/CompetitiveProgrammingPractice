class Solution:
    def dfs(self,board,i,j,visited,trie,current,result,prev):
        if '#' in trie and trie['#']:
            result.append("".join(current))
            trie['#']=False
        nbrs=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        new=trie
        for nbr in nbrs:
            if 0<=nbr[0]<len(board) and 0<=nbr[1]<len(board[0]) and nbr not in visited:
                next_char=board[nbr[0]][nbr[1]]
                if next_char in new:
                    trie=new[next_char] 
                    visited.add(nbr)
                    self.dfs(board,nbr[0],nbr[1],visited,trie,current+[next_char],result,new)
                    visited.remove(nbr)
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dict_trie={}
        for word in words:
            current=dict_trie
            for char in word:
                if char in current:
                    current = current[char]
                else:
                    current[char] = {}
                    current = current[char]
            current['#']=True
        res=[]
        visited=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                char=board[i][j]
                if char in dict_trie:
                    current=[char]
                    trie=dict_trie[char]
                    visited.add((i,j))
                    self.dfs(board,i,j,visited,trie,current,res,dict_trie)
                    visited.remove((i,j))
        return res
                    
                    
