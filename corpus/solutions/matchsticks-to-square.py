class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4 or sum(matchsticks) % 4:
            return False
        target = sum(matchsticks) // 4
        sticks = sorted(matchsticks, reverse=True)
        if sticks[0] > target:
            return False
        sides = [0, 0, 0, 0]

        def place(index: int) -> bool:
            if index == len(sticks):
                return True
            seen = set()
            for side in range(4):
                if sides[side] in seen or sides[side] + sticks[index] > target:
                    continue
                seen.add(sides[side])
                sides[side] += sticks[index]
                if place(index + 1):
                    return True
                sides[side] -= sticks[index]
                if sides[side] == 0:
                    break
            return False

        return place(0)
