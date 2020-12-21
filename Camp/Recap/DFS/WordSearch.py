class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index,i,j,visited):
            nbrs=[[0,1],[0,-1],[1,0],[-1,0]]
            for nbr in nbrs:
                new_i,new_j=i+nbr[0],j+nbr[1]
                if 0<=new_i<len(board) and 0<=new_j<len(board[0])and board[new_i][new_j]==word[index] and (new_i,new_j) not in visited:
                    if index==len(word)-1:
                        return True
                    visited.add((new_i,new_j))
                    if dfs(index+1,new_i,new_j,visited):
                        return True
                    visited.remove((new_i,new_j))
        for i,row in enumerate(board):
            for j,col in enumerate(row):
                if col==word[0]:
                    if len(word)==1:
                        return True
                    visited=set()
                    visited.add((i,j))
                    if dfs(1,i,j,visited):
                        return True
                    visited.remove((i,j))
        return False
    