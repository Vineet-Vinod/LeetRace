class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        scores = defaultdict(list)
        for student, score in items:
            scores[student].append(score)
        return [
            [student, sum(sorted(values, reverse=True)[:5]) // 5]
            for student, values in sorted(scores.items())
        ]
