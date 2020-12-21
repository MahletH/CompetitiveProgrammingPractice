class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen=defaultdict(lambda :-1)
        max_length=0
        unique=-1
        for index,char in enumerate(s):
            unique=max(unique,last_seen[char])
            max_length=max(max_length,index-unique)
            last_seen[char]=index
        return max_length