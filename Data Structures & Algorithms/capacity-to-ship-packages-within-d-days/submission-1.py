class Solution:

    def daysNeededForCap(self, weights: List[int], cap: int) -> int:
        days = 1
        shipment = 0
        
        for weight in weights:
            if shipment + weight > cap:
                days += 1
                shipment = weight
            else:
                shipment += weight

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights) + 1

        while lo < hi:
            mid = (lo + hi) // 2

            if self.daysNeededForCap(weights, mid) <= days:
                hi = mid
            else:
                lo = mid + 1

        return lo
        