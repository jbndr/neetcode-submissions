class Solution:
    def countSort(self, arr):
        m = max(arr)
        freq = [0] * (m+1)

        for val in arr:
            freq[val] += 1

        i = 0
        for val in range(m+1):
            if freq[val]:
                for _ in range(freq[val]):
                    arr[i] = val
                    i += 1
    
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        self.countSort(people)

        left = 0
        right = len(people)-1

        count = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1      
            
        return count