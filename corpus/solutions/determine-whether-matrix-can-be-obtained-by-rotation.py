class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        current = mat
        for _ in range(4):
            if current == target:
                return True
            current = [list(row) for row in zip(*current[::-1])]
        return False
