import collections
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half_size=(len(arr)+1)//2
        removed=rem=0
        count=collections.Counter(arr)
        for key,value in count.most_common():
            removed+=value
            rem+=1            
            if removed>=half_size:
                return rem
        return 0
        