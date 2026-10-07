class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        best = [0] * (len(questions) + 1)
        for index in range(len(questions) - 1, -1, -1):
            points, brainpower = questions[index]
            next_index = min(len(questions), index + brainpower + 1)
            best[index] = max(best[index + 1], points + best[next_index])
        return best[0]
