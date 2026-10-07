class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        difference = [0] * (n + 1)
        for index, value in enumerate(nums):
            if value == 0:
                continue
            start = (index - value + 1) % n
            end = (index + 1) % n
            if start < end:
                difference[start] -= 1
                difference[end] += 1
            else:
                difference[0] -= 1
                difference[end] += 1
                difference[start] -= 1
        score = 0
        best = -n - 1
        answer = 0
        for rotation in range(n):
            score += difference[rotation]
            if score > best:
                best = score
                answer = rotation
        return answer
