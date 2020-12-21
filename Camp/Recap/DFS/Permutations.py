class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(current,result,visited,num):
            visited.remove(num)
            if not visited:
                result.append(current.copy())
            for num in visited:
                current.append(num)
                dfs(current,result,visited.copy(),num)
                current.pop()
        result=[]
        current=[]
        visited=set(nums)
        for num in visited:
            current.append(num)
            dfs(current,result,visited.copy(),num)
            current.pop()
        return result