class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = intervals.sort()
        cur_s, cur_e = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > cur_e:
                result.append([cur_s, cur_e])
                cur_s, cur_e = intervals[i]
            else:
                cur_s = min(cur_s, intervals[i][0])
                cur_e = max(cur_e, intervals[i][1])
        result.append([cur_s, cur_e])
        return result
        