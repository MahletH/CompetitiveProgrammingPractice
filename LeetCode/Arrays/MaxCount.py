class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxCount = 0
        currCount = 0
        nums.append(0)
        for num in nums:
            if num:
                currCount += 1
            elif currCount > maxCount:
                maxCount = currCount
                currCount = 0
            else:
                currCount = 0
        return maxCount