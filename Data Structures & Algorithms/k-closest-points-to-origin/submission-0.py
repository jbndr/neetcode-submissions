import math
import heapq

class Solution:
    def distance(self, point_a, point_b=(0,0)):
        return math.sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.distance(point), point) for point in points]
        heapq.heapify(distances)

        result = []

        for i in range(k):
            result.append(heapq.heappop(distances)[1])

        return result
