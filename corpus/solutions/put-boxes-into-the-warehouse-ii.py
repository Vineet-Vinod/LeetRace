class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        from_left = [0] * n
        from_right = [0] * n
        current = float("inf")
        for index, height in enumerate(warehouse):
            current = min(current, height)
            from_left[index] = current

        current = float("inf")
        for index in range(n - 1, -1, -1):
            current = min(current, warehouse[index])
            from_right[index] = current

        capacities = sorted(max(from_left[i], from_right[i]) for i in range(n))
        boxes.sort()
        box_index = 0
        for capacity in capacities:
            if box_index < len(boxes) and boxes[box_index] <= capacity:
                box_index += 1
        return box_index
