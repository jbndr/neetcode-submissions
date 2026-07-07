class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        buckets = [[] for _ in range(len(nums))]

        for num, freq in counter.items():
            buckets[freq-1] += [num]

        top_k = []
        index = len(buckets) - 1

        while len(top_k) != k:
            top_k.extend(buckets[index])
            index -= 1

        return top_k
