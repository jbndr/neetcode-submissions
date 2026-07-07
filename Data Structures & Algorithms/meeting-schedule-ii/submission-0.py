"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort()

        active = 0
        max_active = 0

        for start, delta in events:
            active += delta
            max_active = max(max_active, active)

        return max_active
        