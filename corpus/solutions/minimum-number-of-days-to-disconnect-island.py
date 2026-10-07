class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cells = {(r, c) for r in range(m) for c in range(n) if grid[r][c]}
        if not cells:
            return 0

        def components(removed):
            unseen = cells - {removed}
            count = 0
            while unseen:
                count += 1
                if count > 1:
                    return count
                stack = [unseen.pop()]
                while stack:
                    r, c = stack.pop()
                    for nxt in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if nxt in unseen:
                            unseen.remove(nxt)
                            stack.append(nxt)
            return count

        if components(None) != 1:
            return 0
        if len(cells) == 1:
            return 1
        for cell in cells:
            if components(cell) != 1:
                return 1
        return 2
