import collections
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_(nums):
            sums=0
            for num in nums:
                sums+=int(num)
            return sums
        digit_sum=collections.defaultdict(list)
        for i in range(1,n+1):
            sums=sum_(str(i))
            digit_sum[sums].append(i)
        val=list(digit_sum.values())
        val.sort(key=lambda x:len(x))
        max_len,max_ind=0,0
        for i,nums in enumerate(val):
            if len(nums)>max_len:
                max_len=len(nums)
                max_ind=i
        return len(val[max_ind:])