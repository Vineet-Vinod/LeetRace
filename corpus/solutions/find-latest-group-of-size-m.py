class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        lengths = [0] * (n + 2)
        groups = 0
        answer = -1
        for step, position in enumerate(arr, 1):
            left, right = lengths[position - 1], lengths[position + 1]
            if left == m:
                groups -= 1
            if right == m:
                groups -= 1
            merged = left + right + 1
            lengths[position - left] = merged
            lengths[position + right] = merged
            if merged == m:
                groups += 1
            if groups:
                answer = step
        return answer
