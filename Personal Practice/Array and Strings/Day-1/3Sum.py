class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=set()
        for i in range(len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                k=-(nums[i])-nums[j]
                if k in seen:
                    pot=[nums[i],nums[j],k]
                    pot.sort()
                    if tuple(pot) not in used:
                        result.append(pot)
                        used.add(tuple(pot))
                seen.add(nums[j])
        return result