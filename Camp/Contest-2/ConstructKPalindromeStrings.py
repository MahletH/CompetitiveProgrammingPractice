import collections
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        count=collections.Counter(s)
        palindrome=0
        for key in count:
            value=count[key]
            if value%2!=0:
                if palindrome>=k:
                    return False
                palindrome+=1            
        return True