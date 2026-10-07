class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        return sum(
            ((count + answer) // (answer + 1)) * (answer + 1)
            for answer, count in counts.items()
        )
