class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)

        starts = []

        for num in nums:
            if num-1 not in values:
                starts.append(num)
        
        longest = 0

        for start in starts:
            running = 1
            current = start

            while True:
                if current+1 in values:
                    running += 1
                    current += 1
                else:
                    break
            
            longest = max(longest, running)
        
        return longest






        