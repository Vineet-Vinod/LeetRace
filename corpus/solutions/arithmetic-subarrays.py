class Solution:
    def checkArithmeticSubarrays(
        self,
        nums: List[int],
        l: List[int],  # noqa: E741 - names match the required candidate keyword interface.
        r: List[int],
    ) -> List[bool]:
        answers: List[bool] = []
        for left, right in zip(l, r):
            values = sorted(nums[left : right + 1])
            difference = values[1] - values[0]
            answers.append(
                all(
                    values[i] - values[i - 1] == difference
                    for i in range(2, len(values))
                )
            )
        return answers
