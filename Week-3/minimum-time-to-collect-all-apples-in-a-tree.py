import collections
class Solution:
    def dfs(self,node,hasApple,tree,visited):
        total=0
        for nbr in tree[node]:
            if nbr not in visited:
                visited.add(nbr)
                total+=self.dfs(nbr,hasApple,tree,visited)
        if total and node!=0:
            total+=1
        elif node!=0 and hasApple[node]:
            total=1
        return total
    def minTime(self, n: int, edges, hasApple) -> int:
        tree=defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        visited=set([0])
        return self.dfs(0,hasApple,tree,visited)*2
                