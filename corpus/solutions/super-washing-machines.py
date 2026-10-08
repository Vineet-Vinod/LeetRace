class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        if total % len(machines):
            return -1
        average = total // len(machines)
        prefix = answer = 0
        for value in machines:
            excess = value - average
            prefix += excess
            answer = max(answer, abs(prefix), excess)
        return answer
