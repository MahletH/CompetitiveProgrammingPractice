class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        count=Counter(s)
        palindrome=0
        for key,value in count.items():
            if value%2!=0:
                palindrome+=1  
        if palindrome>k:
            return False          
        return True
