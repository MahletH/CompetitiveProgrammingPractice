class Solution:
    def findNumbers(self, nums):
        even_digits=0
        for num in nums:
            if num<10:
                continue
            elif num<100:
                even_digits+=1
            elif num<1000:
                continue
            elif num<10000:
                even_digits+=1
            else:
                if num==100000:
                    even_digits+=1
                continue
        return even_digits