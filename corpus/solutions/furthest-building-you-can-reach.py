class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        climbs = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heappush(climbs, climb)
            if len(climbs) > ladders:
                bricks -= heappop(climbs)
                if bricks < 0:
                    return i
        return len(heights) - 1
