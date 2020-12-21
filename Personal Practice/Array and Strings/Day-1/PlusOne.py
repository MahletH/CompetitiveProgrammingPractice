class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        res=[]
        i=len(digits)-1
        while i>=0:
            carry+=digits[i]
            res.append((carry)%10)
            carry//=10
            i-=1
        if carry:
            res.append(carry)
        return reversed(res)