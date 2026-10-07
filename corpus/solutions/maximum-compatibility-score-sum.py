class Solution:
    def maxCompatibilitySum(
        self, students: List[List[int]], mentors: List[List[int]]
    ) -> int:
        n = len(students)
        scores = [
            [sum(a == b for a, b in zip(student, mentor)) for mentor in mentors]
            for student in students
        ]
        dp = {0: 0}
        for student in range(n):
            next_dp = {}
            for mask, total in dp.items():
                for mentor in range(n):
                    if not mask >> mentor & 1:
                        new_mask = mask | (1 << mentor)
                        next_dp[new_mask] = max(
                            next_dp.get(new_mask, 0), total + scores[student][mentor]
                        )
            dp = next_dp
        return dp[(1 << n) - 1]
