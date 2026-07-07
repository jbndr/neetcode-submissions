class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        left = 0
        right = len(people)-1

        count = 0
        while right >= 0 and people[right] >= limit:
            count += 1
            right -= 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1
                
            
        return count

        


