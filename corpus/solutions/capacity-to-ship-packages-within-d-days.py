class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        while low < high:
            capacity = (low + high) // 2
            used_days = 1
            load = 0
            for weight in weights:
                if load + weight > capacity:
                    used_days += 1
                    load = 0
                load += weight
            if used_days <= days:
                high = capacity
            else:
                low = capacity + 1
        return low
