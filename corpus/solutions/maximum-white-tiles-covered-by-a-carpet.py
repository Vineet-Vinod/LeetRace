class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        best = 0
        covered = 0
        right = 0
        for left in range(len(tiles)):
            start = tiles[left][0]
            end = start + carpetLen - 1
            while right < len(tiles) and tiles[right][1] <= end:
                covered += tiles[right][1] - tiles[right][0] + 1
                right += 1
            current = covered
            if right < len(tiles) and tiles[right][0] <= end:
                current += end - tiles[right][0] + 1
            best = max(best, current)
            if right > left:
                covered -= tiles[left][1] - tiles[left][0] + 1
            else:
                right = left + 1
        return best
