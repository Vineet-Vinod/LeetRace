class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        ranked = []
        for feedback, student in zip(report, student_id):
            score = sum(
                3 if word in positive else -1 if word in negative else 0
                for word in feedback.split()
            )
            ranked.append((-score, student))
        ranked.sort()
        return [student for _, student in ranked[:k]]
