"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(intervals, key= lambda x: x.start)

        end = sorted(intervals, key= lambda x: x.end)
        n = len(intervals)

        count = 0
        res = 0

        s, e = 0, 0
        while s < n and e < n:

            if start[s].start < end[e].end:
                count += 1
                s += 1
                res = max(count, res)
            else:
                count -= 1
                e += 1
        
        return res

