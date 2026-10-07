class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
    ) -> int:
        hours = max(0, sum(energy) + 1 - initialEnergy)
        current = initialExperience
        for opponent in experience:
            if current <= opponent:
                hours += opponent + 1 - current
                current = opponent + 1
            current += opponent
        return hours
