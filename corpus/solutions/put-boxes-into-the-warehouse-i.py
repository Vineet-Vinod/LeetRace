class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        effective = []
        minimum = float("inf")
        for height in warehouse:
            minimum = min(minimum, height)
            effective.append(minimum)
        boxes.sort()
        box_index = 0
        fitted = 0
        for height in reversed(effective):
            if box_index < len(boxes) and boxes[box_index] <= height:
                box_index += 1
                fitted += 1
        return fitted
