class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def dfs(i,j):
            A[i][j]=0
            nbrs=[[0,1],[0,-1],[1,0],[-1,0]]
            for nbr in nbrs:
                new_i,new_j=i+nbr[0],j+nbr[1]
                if 0<=new_i<=len(A)-1 and 0<=new_j<=len(A[0])-1 and A[new_i][new_j]:
                    dfs(new_i,new_j)
                             
        enclaves=0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i==0 or i==len(A)-1 or j==0 or j==len(A[0])-1:
                    if A[i][j]:
                        dfs(i,j)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    enclaves+=1
        return enclaves