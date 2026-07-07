import math
import heapq

class Solution:
    def distance(self, point_a, point_b=(0,0)):
        return (point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            distance = self.distance(point)
            heapq.heappush(maxHeap, [-distance, point])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [point for dist, point in maxHeap]
