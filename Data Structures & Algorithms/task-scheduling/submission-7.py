from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [(-count, item) for item, count in counter.items()]
        heapq.heapify(heap)
        cooldown = deque([])

        ticks = 0

        while heap or cooldown:
            if cooldown and cooldown[0][0] < ticks:
                next_available, count, item = cooldown.popleft()
                heapq.heappush(heap, (count, item))

            if heap:
                count, item = heapq.heappop(heap)
                if -count > 1:
                    cooldown.append((ticks + n, count+1, item))

            ticks += 1

        return ticks