class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            cur_s, cur_e = intervals[i]
            if cur_s > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > cur_e:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], cur_s), max(newInterval[1], cur_e)]
        result.append(newInterval)
        return result
