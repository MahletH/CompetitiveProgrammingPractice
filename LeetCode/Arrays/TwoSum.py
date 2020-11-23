class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited={}
        for i,num in enumerate(nums):
            if target-num in visited:
                return [i,visited.get(target-num)]
            visited[num]=i