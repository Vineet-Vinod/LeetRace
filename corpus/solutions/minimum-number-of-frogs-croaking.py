class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        stages = [0] * 5
        active = 0
        maximum = 0
        index = {char: i for i, char in enumerate("croak")}
        for char in croakOfFrogs:
            stage = index.get(char, -1)
            if stage < 0:
                return -1
            if stage == 0:
                stages[0] += 1
                active += 1
                maximum = max(maximum, active)
            else:
                if stages[stage - 1] == 0:
                    return -1
                stages[stage - 1] -= 1
                if stage == 4:
                    active -= 1
                else:
                    stages[stage] += 1
        return maximum if active == 0 and sum(stages[:4]) == 0 else -1
