class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        if len(intervals) == 1:
            return 0
        intervals.sort()
        cur_e = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if s < cur_e:
                result += 1
                cur_e = min(e, cur_e)
            else:
                cur_e = e
        return result