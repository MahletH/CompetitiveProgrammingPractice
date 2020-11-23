class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        cookie_count=0
        kid_count=0
        g.sort()
        s.sort()
        
        while cookie_count<len(s) and kid_count<len(g):
            if(s[cookie_count]>=g[kid_count]):
                kid_count += 1
            cookie_count += 1
        return kid_count