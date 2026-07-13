class Solution:

    def daysToShipWithCap(self, weights, days, cap):
        days = 1
        shipment = 0

        for weight in weights:
            if weight > cap:
                return float("inf")

            if shipment + weight > cap:
                days += 1
                shipment = weight
            else:
                shipment += weight

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = 1
        hi = sum(weights)+1

        while lo < hi:
            mid = (lo + hi) // 2

            if self.daysToShipWithCap(weights, days, mid) <= days:
                hi = mid
            else:
                lo = mid + 1

        return ((lo+hi) // 2)
        