class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        start_end={}
        for i,char in enumerate(S):
            if char in start_end:
                start_end[char][1]=i
            else:
                start_end[char]=[i,i]
        intervals=list(start_end.values())
        stack=[]
        for interval in intervals:
            if stack and stack[-1][1]>interval[0]:
                stack[-1][1]=max(interval[1],stack[-1][1])
            else:
                stack.append(interval)
        partitions=[]
        for interval in stack:
            partitions.append(interval[1]-interval[0]+1)
        return partitions
        