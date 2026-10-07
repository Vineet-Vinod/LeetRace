class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        for boxes, units in sorted(boxTypes, key=lambda pair: pair[1], reverse=True):
            loaded = min(boxes, truckSize)
            total += loaded * units
            truckSize -= loaded
            if truckSize == 0:
                break
        return total
