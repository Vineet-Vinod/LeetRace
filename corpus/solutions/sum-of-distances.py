class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        positions: dict[int, list[int]] = {}
        for index, value in enumerate(nums):
            positions.setdefault(value, []).append(index)
        answer = [0] * len(nums)
        for indices in positions.values():
            prefix = 0
            total = sum(indices)
            for offset, index in enumerate(indices):
                left = index * offset - prefix
                right = (total - prefix - index) - index * (len(indices) - offset - 1)
                answer[index] = left + right
                prefix += index
        return answer
