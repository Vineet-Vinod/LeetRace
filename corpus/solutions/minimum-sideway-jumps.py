class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        jumps = [1, 0, 1]
        for obstacle in obstacles[1:]:
            if obstacle:
                jumps[obstacle - 1] = 10**9
            best = min(jumps) + 1
            for lane in range(3):
                if lane != obstacle - 1:
                    jumps[lane] = min(jumps[lane], best)
        return min(jumps)
