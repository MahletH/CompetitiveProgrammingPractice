class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_area=0
        while i<j:
            area=min(height[i],height[j])*(j-i)
            max_area=max(max_area,area)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return max_area