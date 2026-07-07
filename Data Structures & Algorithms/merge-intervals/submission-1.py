class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            start_1, end_1 = result[-1]
            start_2, end_2 = intervals[i]

            if start_2 <= end_1:
                result[-1][1] = max(end_1, end_2)
            else:
                result.append(intervals[i])

        return result
        