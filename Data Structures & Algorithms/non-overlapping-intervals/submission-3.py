class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 1. Sort by end times in ASCENDING order
        intervals.sort(key=lambda x: x[1])

        erase_count = 0
        # 2. Track the end time of the last successfully kept interval
        last_end = intervals[0][1]

        # 3. Iterate through the rest
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # If the current interval starts BEFORE the last one ends, it's an overlap!
            if start < last_end:
                erase_count += 1
            else:
                # No overlap, so we keep it and update our boundary
                last_end = end

        return erase_count