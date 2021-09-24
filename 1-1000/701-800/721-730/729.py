class MyCalendar:

    def __init__(self):
        self.events = []
        return
        

    def book(self, start: int, end: int) -> bool:
        left, right = 0, len(self.events)
        while left < right:
            mid = (left + right) >> 1
            if start < self.events[mid][1]:
                right = mid
            else:
                left = mid + 1
        index = right
        if index == len(self.events):
            self.events.append((start, end))
            return True
        if end > self.events[index][0]:
            return False

        self.events.insert(index, (start, end))
        return True
