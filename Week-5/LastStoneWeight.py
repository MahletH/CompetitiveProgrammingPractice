import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            dif=abs(heapq.heappop(heap)-heapq.heappop(heap))
            if dif:
                heapq.heappush(heap,-dif)
        if heap:
            return abs(heapq.heappop(heap)) 
        return 0