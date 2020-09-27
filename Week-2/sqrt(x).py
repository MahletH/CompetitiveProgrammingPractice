class Solution:
    def mySqrt(self, x: int) -> int:
        start,end=1,x
        while start<end-1:
            current=start+(end-start)//2
            if current**2==x:
                return current
            if current**2<x:
                start=current+1
            else:
                end=current
        if start**2<=x:
            return start
        return start-1