class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        lengths = [[0] * k for _ in range(k)]
        answer = 1
        for value in nums:
            residue = value % k
            for previous in range(k):
                lengths[previous][residue] = lengths[residue][previous] + 1
                answer = max(answer, lengths[previous][residue])
        return answer
