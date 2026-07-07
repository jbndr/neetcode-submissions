class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        result = [k for k, _ in sorted(counter.items(), key=lambda item: item[1], reverse=True)]

        return result[:k]