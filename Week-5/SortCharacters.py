from collections import heapq,Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        
        for key,value in counter.items():
            heapq.heappush(heap, (-value, key))
            
        result = []
        while heap:
            value, char = heapq.heappop(heap)
            result.append(-value * char) 
            
        return "".join(result)