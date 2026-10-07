class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        words = [phrase.split() for phrase in phrases]
        answers = set()
        for i, first in enumerate(words):
            for j, second in enumerate(words):
                if i != j and first[-1] == second[0]:
                    answers.add(" ".join(first + second[1:]))
        return sorted(answers)
