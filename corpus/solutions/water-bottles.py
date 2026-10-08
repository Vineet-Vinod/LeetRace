class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = empty = numBottles
        while empty >= numExchange:
            exchanged = empty // numExchange
            total += exchanged
            empty = empty % numExchange + exchanged
        return total
