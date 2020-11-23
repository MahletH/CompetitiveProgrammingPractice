class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        sums=sum(nums)
        prefix=[0 for i in range(len(nums))]
        suffix=[0 for i in range(len(nums))]
        prefix[0]=nums[0]
        suffix[-1]=nums[-1]
        for i in range(1,len(nums)):
            if i==1:
                prefix[i]=nums[i]
                suffix[len(nums)-1-i]=nums[len(nums)-1-i]
            else:
                prefix[i]=prefix[i-2]+nums[i]
                suffix[len(nums)-1-i]=suffix[len(nums)-i+1]+nums[len(nums)-1-i]
        ways=0
        for i in range(1,len(nums)-1):
            if i==len(nums)-2:
                if prefix[i-1]==(sums-nums[i])/2:
                    ways+=1
            elif prefix[i-1]+suffix[i+2]==(sums-nums[i])/2:
                ways+=1
        if suffix[1]==(sums-nums[0])/2:
            ways+=1
        if prefix[-2]==(sums-nums[-1])/2:
            ways+=1
        return ways