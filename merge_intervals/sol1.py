from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        intervals.sort()
        upd_intervals = [intervals[0]]
        i = 0
        n = len(intervals)

        while i < n - 1:
            
            if upd_intervals[-1][1] >= intervals[i+1][0] or upd_intervals[-1][1]  == intervals[i+1][0]:
                
                upd_intervals[-1][1] = max(upd_intervals[-1][1], intervals[i+1][1])
            else:
                
                upd_intervals.append(intervals[i+1])
            
            
            i += 1
        return upd_intervals