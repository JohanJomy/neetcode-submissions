class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = newInterval[0]
        i = 0

        while i < len(intervals) and intervals[i][0] < s:
            i += 1

        if i > 0 and intervals[i-1][1] >= newInterval[0]:
            newInterval = [intervals[i-1][0], max(intervals[i-1][1], newInterval[1])]
            i -= 1
            intervals.pop(i)
        # print(intervals, newInterval, i, i < len(intervals)-1)

        while i <= len(intervals)-1 and newInterval[1] >= intervals[i][0]:
            # print(True)
            newInterval = [newInterval[0], max(intervals[i][1], newInterval[1])]
            intervals.pop(i)
        
        intervals.insert(i, newInterval)

        return intervals


            