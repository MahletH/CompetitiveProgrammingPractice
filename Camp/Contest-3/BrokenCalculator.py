class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        path=0
        while Y>X:
            path+=1
            if Y%2: Y+=1
            else: Y//=2
        return path+X-Y
