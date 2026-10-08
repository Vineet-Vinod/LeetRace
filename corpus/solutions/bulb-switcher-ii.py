class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        initial = (1, 1, 1, 1, 1, 1)
        buttons = (
            (0, 0, 0, 0, 0, 0),
            (1, 0, 1, 0, 1, 0),
            (0, 1, 0, 1, 0, 1),
            (1, 0, 0, 1, 0, 0),
        )
        states = {initial}
        for _ in range(presses):
            states = {
                tuple(a ^ b for a, b in zip(state, button))
                for state in states
                for button in buttons
            }
        return len({state[: min(n, 6)] for state in states})
