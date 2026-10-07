class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        values = list(dominoes)
        forces = [0] * len(values)
        force = 0
        for i, char in enumerate(values):
            if char == "R":
                force = len(values)
            elif char == "L":
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force
        force = 0
        for i in range(len(values) - 1, -1, -1):
            if values[i] == "L":
                force = len(values)
            elif values[i] == "R":
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force
        return "".join(
            "R" if force > 0 else "L" if force < 0 else "." for force in forces
        )
