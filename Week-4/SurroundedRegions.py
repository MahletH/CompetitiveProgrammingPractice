class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j,visited):
            if (i,j) not in visited and i>=0 and i<len(board) and j>=0 and j<len(board[0]):
                if board[i][j]=="O":
                    visited.add((i,j))
                    dfs(i+1,j,visited)
                    dfs(i-1,j,visited)
                    dfs(i,j+1,visited)
                    dfs(i,j-1,visited)
        visited=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not i or not j or i==len(board)-1 or j==len(board[0])-1:
                    if board[i][j]=="O":
                        dfs(i,j,visited)
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if (i,j) not in visited and board[i][j]=="O":
                    board[i][j]="X"