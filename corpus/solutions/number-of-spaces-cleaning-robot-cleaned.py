class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        rows, cols = len(room), len(room[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        row = col = direction = 0
        states = set()
        cleaned = set()
        while (row, col, direction) not in states:
            states.add((row, col, direction))
            cleaned.add((row, col))
            dr, dc = directions[direction]
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or room[nr][nc] == 1:
                direction = (direction + 1) % 4
            else:
                row, col = nr, nc
        return len(cleaned)
