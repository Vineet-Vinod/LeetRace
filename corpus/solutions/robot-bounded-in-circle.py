class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = direction = 0
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for instruction in instructions:
            if instruction == "G":
                dx, dy = directions[direction]
                x += dx
                y += dy
            elif instruction == "L":
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
        return (x, y) == (0, 0) or direction != 0
