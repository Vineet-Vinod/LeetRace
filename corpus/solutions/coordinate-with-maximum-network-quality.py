class Solution:
    def bestCoordinate(self, towers: list[list[int]], radius: int) -> list[int]:
        best_quality = -1
        best = [0, 0]
        for x in range(51 + radius):
            for y in range(51 + radius):
                quality = 0
                for tx, ty, strength in towers:
                    distance = math.sqrt((x - tx) ** 2 + (y - ty) ** 2)
                    if distance <= radius:
                        quality += int(strength / (1 + distance))
                if quality > best_quality:
                    best_quality = quality
                    best = [x, y]
        return best
