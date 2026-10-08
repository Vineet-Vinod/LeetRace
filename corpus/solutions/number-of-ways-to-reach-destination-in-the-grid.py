class Solution:
    def numberOfWays(
        self, n: int, m: int, k: int, source: List[int], dest: List[int]
    ) -> int:
        mod = 10**9 + 7
        # Four states encode whether the row and column match the destination.
        states = [0] * 4
        states[2 * int(source[0] == dest[0]) + int(source[1] == dest[1])] = 1
        for _ in range(k):
            next_states = [0] * 4
            for state, count in enumerate(states):
                row, col = divmod(state, 2)
                if row:
                    next_states[col] += count * (n - 1)
                else:
                    next_states[2 + col] += count
                    next_states[col] += count * (n - 2)
                if col:
                    next_states[2 * row] += count * (m - 1)
                else:
                    next_states[2 * row + 1] += count
                    next_states[2 * row] += count * (m - 2)
            states = [value % mod for value in next_states]
        return states[3]
