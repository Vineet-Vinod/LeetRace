class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = {tuple(point) for point in obstacles}
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = 0
        x = y = 0
        farthest = 0
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                dx, dy = directions[direction]
                for _ in range(command):
                    if (x + dx, y + dy) in blocked:
                        break
                    x += dx
                    y += dy
                    farthest = max(farthest, x * x + y * y)
        return farthest
