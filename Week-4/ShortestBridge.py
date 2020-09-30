from collections import deque
class Solution:
    def shortestBridge(self, A) -> int:
        def dfs(i,j,que,visited):
            if (i,j) not in visited and i>=0 and i<len(A) and j>=0 and j<len(A[0]) and A[i][j]:
                que.append((i,j,0))
                visited.add((i,j))                
                dfs(i-1,j,que,visited)
                dfs(i+1,j,que,visited)
                dfs(i,j-1,que,visited)
                dfs(i,j+1,que,visited)
        def bfs(que,visited):
            nbrs=[[1,0],[-1,0],[0,1],[0,-1]]
            while que:
                cur=que.popleft()
                for nbr in nbrs:
                    i,j=cur[0]+nbr[0],cur[1]+nbr[1]
                    if i>=0 and i<len(A) and j>=0 and j<len(A[0]) and (i,j) not in visited:
                        if A[i][j]:
                            return cur[2]
                        que.append((i,j,cur[2]+1))
                        visited.add((i,j))
                        
        que=deque()
        visited=set()
        for i,land in enumerate(A):
            for j,num in enumerate(land):
                if num:
                    dfs(i,j,que,visited)
                    return bfs(que,visited)