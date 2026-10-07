class Solution:
    def countCollisions(self, directions: str) -> int:
        left = 0
        right = len(directions) - 1
        while left <= right and directions[left] == "L":
            left += 1
        while left <= right and directions[right] == "R":
            right -= 1
        return sum(direction != "S" for direction in directions[left : right + 1])
