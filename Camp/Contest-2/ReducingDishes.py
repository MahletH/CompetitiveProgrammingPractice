class Solution:
    def maxSatisfaction(self, satisfactions: list[int]) -> int:
        satisfactions.sort()
        result=0
        current=0
        for satisfaction in reversed(satisfactions):
            current+=satisfaction
            if current<0:
                break
            result+=current
        return result