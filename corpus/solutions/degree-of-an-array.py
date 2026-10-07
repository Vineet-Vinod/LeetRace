class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first: dict[int, int] = {}
        counts: dict[int, int] = {}
        degree = 0
        answer = len(nums)
        for index, value in enumerate(nums):
            first.setdefault(value, index)
            counts[value] = counts.get(value, 0) + 1
            if counts[value] > degree:
                degree = counts[value]
                answer = index - first[value] + 1
            elif counts[value] == degree:
                answer = min(answer, index - first[value] + 1)
        return answer
