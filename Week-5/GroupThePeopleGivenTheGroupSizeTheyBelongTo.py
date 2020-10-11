import heapq
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        heap=[]
        output=[]
        for i,groupSize in enumerate(groupSizes):
            heapq.heappush(heap,(groupSize,i))
        while heap:
            cur_list=[]
            cur=heapq.heappop(heap)
            cur_list.append(cur[1])
            while len(cur_list)<cur[0]:
                cur_list.append(heapq.heappop(heap)[1])
            output.append(cur_list)
        return output
                