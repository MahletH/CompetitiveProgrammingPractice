import collections
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        count=collections.Counter(nums)
        for key in nums:
            if count[key]:
                prev=key+1
                while prev<key+k:
                    if count[prev]-count[key]<0:
                        return False
                    count[prev]-=count[key]
                    prev+=1
                count[key]=0
        return True
        