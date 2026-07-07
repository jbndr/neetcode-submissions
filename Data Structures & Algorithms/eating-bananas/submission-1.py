class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        m = max(piles)

        left = 1
        right = m + 1

        def can_i_eat_within_hours(piles, h, rate):
            hours = 0
            for p in piles:
                hours += p // rate
                if p % rate != 0:
                    hours += 1
                if hours > h:
                    return False
            
            return True


        while left < right:
            mid = left + (right-left)//2

            if can_i_eat_within_hours(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left