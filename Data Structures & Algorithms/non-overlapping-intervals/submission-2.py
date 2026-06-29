class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        # print(intervals)
        last = intervals[0]
        res = 0
        for s, e in intervals[1:]:
            # overlap
            if last[1] > s:
                res += 1
                if last[1] > e:
                    last = [s, e]
            else:
                last = [s, e]
            
            # print(s, e, last)
        
        return res
                