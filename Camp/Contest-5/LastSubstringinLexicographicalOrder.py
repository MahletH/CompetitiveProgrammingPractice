class Solution:
    def lastSubstring(self, s: str) -> str:
        start,next_,k=0,1,0
        while next_+k<len(s):
            if s[start+k]==s[next_+k]:
                k+=1
                continue
            elif s[start+k]<s[next_+k]:
                start=next_
                next_+=1
            else:
                next_=next_+k+1
            k=0
        return s[start:]
