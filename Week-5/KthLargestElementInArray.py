import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=[]
        for num in nums:
            heapq.heappush(heap,-num)
        for i in range(k-1):
            heapq.heappop(heap)
        return -1*(heapq.heappop(heap))