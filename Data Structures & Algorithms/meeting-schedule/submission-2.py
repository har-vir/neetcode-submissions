"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        latestEnd = 0

        intervals = sorted(intervals, key=lambda x: x.start)


        for i in intervals:
            if i.start < latestEnd:
                return False
            if i.end > latestEnd:
                latestEnd = i.end
        
        return True
