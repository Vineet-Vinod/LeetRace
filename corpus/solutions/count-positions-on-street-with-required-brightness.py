class Solution:
    def meetRequirement(
        self, n: int, lights: List[List[int]], requirement: List[int]
    ) -> int:
        delta = [0] * (n + 1)
        for position, radius in lights:
            left, right = max(0, position - radius), min(n - 1, position + radius)
            delta[left] += 1
            delta[right + 1] -= 1
        answer = brightness = 0
        for i, required in enumerate(requirement):
            brightness += delta[i]
            answer += brightness >= required
        return answer
