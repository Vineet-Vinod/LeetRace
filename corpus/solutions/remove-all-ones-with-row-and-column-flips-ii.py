class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cells = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c]]
        if not cells:
            return 0
        operations: list[tuple[int, int]] = []
        for selected, (r, c) in enumerate(cells):
            mask = 0
            for i, (rr, cc) in enumerate(cells):
                if rr == r or cc == c:
                    mask |= 1 << i
            operations.append((mask, 1 << selected))
        full = (1 << len(cells)) - 1
        queue = deque([(full, 0)])
        seen = {full}
        while queue:
            state, steps = queue.popleft()
            if state == 0:
                return steps
            for mask, selected_bit in operations:
                if not state & selected_bit:
                    continue
                nxt = state & ~mask
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1
