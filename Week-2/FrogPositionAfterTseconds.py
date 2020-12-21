class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree=defaultdict(set)
        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])
        def dfs(current_index,total,t,probablity,max_,visited,parent):
            if t>total:
                return max_
            nbrs=(tree[current_index])
            length=len(nbrs)- (parent is not None)
            if current_index==target and (t==total or not length):
                return probablity
            visited.add(current_index)
            for nbr in nbrs:
                if nbr not in visited:
                    max_=max(max_,dfs(nbr,total,t+1,probablity*(1/length),max_,visited,current_index))
            return max_
        return dfs(1,t,0,1,0,set(),None)