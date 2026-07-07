class Solution:

    def merge(self, intervals):
        print(intervals)

        if len(intervals) == 0:
            return []

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            start_1, end_1 = result[-1]
            start_2, end_2 = interval
            if end_1 >= start_2:
                result[-1] = [start_1, max(end_1, end_2)]
            else:
                result.append(intervals[i])

        return result

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_new, end_new = newInterval

        inserted_intervals = []

        for i, interval in enumerate(intervals):
            start, end = interval
            if start_new < start or start_new <= start and end_new <= end:
                left = intervals[:i]
                right = intervals[i:]
                inserted_intervals = left + [newInterval] + right
                break

        if len(inserted_intervals) <= len(intervals):
            inserted_intervals = intervals + [newInterval]

        return self.merge(inserted_intervals)
        
        