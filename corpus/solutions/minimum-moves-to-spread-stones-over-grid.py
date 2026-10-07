class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        extra = [
            (r, c)
            for r in range(3)
            for c in range(3)
            for _ in range(max(0, grid[r][c] - 1))
        ]
        empty = [
            (r, c)
            for r in range(3)
            for c in range(3)
            for _ in range(max(0, 1 - grid[r][c]))
        ]
        costs = [[abs(r - er) + abs(c - ec) for er, ec in empty] for r, c in extra]
        best_for_mask = {0: 0}
        for row in costs:
            updated: dict[int, int] = {}
            for mask, cost in best_for_mask.items():
                for target, move_cost in enumerate(row):
                    bit = 1 << target
                    if mask & bit:
                        continue
                    next_mask = mask | bit
                    next_cost = cost + move_cost
                    updated[next_mask] = min(updated.get(next_mask, 10**9), next_cost)
            best_for_mask = updated
        return best_for_mask.get((1 << len(empty)) - 1, 0)
