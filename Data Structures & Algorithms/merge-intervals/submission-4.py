class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start <= last_end: #time to merge
                to_append = max(last_end, end)
                res[-1][1] = to_append
            else:
                res.append([start,end])
        return res