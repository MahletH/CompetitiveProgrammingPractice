class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited=set()
        new_target=list(target)
        for i,num in enumerate(new_target):
            new_target[i]=int(num)
        new_target=tuple(new_target)
        for deadend in deadends:
            new=list(deadend)
            for i,num in enumerate(new):
                new[i]=int(num)
            visited.add(tuple(new))
        start=(0,0,0,0)
        que=collections.deque()
        if start not in visited:
            que.append((start,0))
            while que:
                new,flip=que.popleft()
                if new_target==new:
                    return flip
                next_=[(new[0],new[1],new[2],(new[3]+1)%10),
                       (new[0],new[1],new[2],(new[3]-1)%10), 
                       (new[0],new[1],(new[2]+1)%10,new[3]),
                       (new[0],new[1],(new[2]-1)%10,new[3]),
                       (new[0],(new[1]+1)%10,new[2],new[3]),
                       (new[0],(new[1]-1)%10,new[2],new[3]), 
                       ((new[0]+1)%10,new[1],new[2],new[3]),
                       ((new[0]-1)%10,new[1],new[2],new[3])]
                for next_m in next_:
                    if next_m not in visited:
                        visited.add(next_m)
                        que.append((next_m,flip+1))
        return -1
                    