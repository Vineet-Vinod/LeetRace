class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        day = 0
        state = tuple(cells)
        while day < n and state not in seen:
            seen[state] = day
            next_state = [0] * 8
            for i in range(1, 7):
                next_state[i] = int(state[i - 1] == state[i + 1])
            state = tuple(next_state)
            day += 1
        if day < n:
            cycle = day - seen[state]
            remaining = (n - day) % cycle
            for _ in range(remaining):
                state = tuple(
                    [0] + [int(state[i - 1] == state[i + 1]) for i in range(1, 7)] + [0]
                )
        return list(state)
