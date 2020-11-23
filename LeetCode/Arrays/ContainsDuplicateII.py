class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numFoundAt={}
        for i,num in enumerate(nums):
            if num in numFoundAt and abs(numFoundAt[num]-i)<=k:
                return True
            numFoundAt[num]=i
        return False
        