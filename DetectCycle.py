class Solution:
    def dfs(self, grid,visited,parent,current):
        if current in visited:
            return True
        visited.add(current)
        nbrs=[(current[0]+1,current[1]),(current[0]-1,current[1]),(current[0],current[1]+1),(current[0],current[1]-1)]
        for nbr in nbrs:
            if 0<=nbr[0]<len(grid) and 0<=nbr[1]<len(grid[0]) and parent!=nbr and grid[nbr[0]][nbr[1]]==grid[current[0]][current[1]]:
                is_cycle=self.dfs(grid,visited,current,nbr)
                if is_cycle:
                    return True
        return False
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited=set()
        for i,row in enumerate(grid):
            for j in range(len(row)):
                if (i,j) not in visited:
                    is_cycle=self.dfs(grid,visited,(None,None),(i,j))
                    if is_cycle:
                        return True
        return False
        
