class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        positions = {}
        for index, value in enumerate(nums):
            positions.setdefault(value, []).append(index)

        n = len(nums)
        answer = n
        for indices in positions.values():
            gaps = [indices[i + 1] - indices[i] for i in range(len(indices) - 1)]
            gaps.append(indices[0] + n - indices[-1])
            answer = min(answer, max(gaps) // 2)
        return answer
