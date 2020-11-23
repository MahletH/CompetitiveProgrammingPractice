class MyCalendarTwo:

    def __init__(self):
        self.singles=[]
        self.doubles=[]
    def book(self, start: int, end: int) -> bool:
        if not self.singles:
            self.singles.append((start,end))
        else:
            for slot in self.doubles:
                if slot[1]>start and end>slot[0]:
                    return False
            for slot in self.singles:
                if slot[1]>start and end>slot[0]:
                    self.doubles.append((max(slot[0],start),min(slot[1],end)))
            self.singles.append((start,end))
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)