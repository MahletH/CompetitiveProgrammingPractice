class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res=[]
        while k:
            if (n-len(res))*26-k>=26:
                res.append("a")
                k-=1
            elif 0<(n-len(res))*26-k<26:
                res.append(chr(ord("a")+k%26-1))
                k-=k%26
            else:
                k-=26
                res.append("z")
        return "".join(res)
        