from collections import heapq,Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        letters=list(S)
        count=Counter(letters)
        heap=[]
        for char in count:
            heapq.heappush(heap,(-count[char],char))
        result=[]
        current=heapq.heappop(heap)
        while heap:
            result.append(current[1])
            next_=heapq.heappop(heap)
            if current[0]!=-1:
                heapq.heappush(heap,(current[0]+1,current[1]))
            current=next_
        if current[0]!=-1:
            return ""
        result.append(current[1])
        return "".join(result)