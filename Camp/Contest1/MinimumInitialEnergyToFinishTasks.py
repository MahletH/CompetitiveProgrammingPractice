class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        min_=0        
        for task in tasks:
            min_+=task[0]
        minimum_effort=min_
        tasks.sort(key=lambda x:x[0]-x[1])   
        for task in tasks:
            if min_>=task[1]:
                min_-=task[0]
            else:
                minimum_effort+=(task[1]-min_)
                min_=task[1]
                min_-=task[0]
        return minimum_effort