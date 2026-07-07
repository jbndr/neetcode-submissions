import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]

        heap = []

        for idx, num in enumerate(stones):
            heapq.heappush(heap, (num, idx))

            if len(heap) > 2:
                heapq.heappop(heap)

        idx_1 = heap[0][1]
        idx_2 = heap[1][1]

        new_stones = [x for idx, x in enumerate(stones) if idx not in [idx_1, idx_2]]

        if heap[0][0] != heap[1][0]:
            new_stones.append(heap[1][0]-heap[0][0])

        return self.lastStoneWeight(new_stones)
        