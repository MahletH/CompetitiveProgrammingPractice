from collections import heapq
class Solution:
    def sortArray(self, nums):
        sorted_list=[]
        heapq.heapify(nums)
        return [(heapq.heappop(nums)) for i in range(len(nums))]