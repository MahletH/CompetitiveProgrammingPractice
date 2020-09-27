class Solution:
    def searchInsert(self, nums, target) -> int:
        start,end=0,len(nums)-1
        while start<end:
            cur=start+(end-start)//2
            if nums[cur]==target:
                return cur
            elif nums[cur]<target:
                start=cur+1
            else:
                end=cur
        if nums[start]<target:
            return start+1
        return start