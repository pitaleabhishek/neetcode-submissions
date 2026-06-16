class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        result = [intervals[0]]
        count = 0
        prev_end = result[-1][1]
        for interval in intervals[1:]:
            
            if interval[0] >= prev_end:
                prev_end = interval[1]
            else:
                count += 1

        return count

