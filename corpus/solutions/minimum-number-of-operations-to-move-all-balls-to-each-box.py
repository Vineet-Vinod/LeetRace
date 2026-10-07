class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
        balls = moves = 0
        for index, value in enumerate(boxes):
            result[index] += moves
            balls += value == "1"
            moves += balls
        balls = moves = 0
        for index in range(len(boxes) - 1, -1, -1):
            result[index] += moves
            balls += boxes[index] == "1"
            moves += balls
        return result
