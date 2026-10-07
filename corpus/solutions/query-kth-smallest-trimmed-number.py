class Solution:
    def smallestTrimmedNumbers(
        self, nums: list[str], queries: list[list[int]]
    ) -> list[int]:
        answers = []
        for rank, trim in queries:
            order = sorted(
                range(len(nums)), key=lambda index: (nums[index][-trim:], index)
            )
            answers.append(order[rank - 1])
        return answers
