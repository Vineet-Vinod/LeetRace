from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        values = [str(value) for value in nums]
        values.sort(
            key=cmp_to_key(
                lambda left, right: (
                    (right + left > left + right) - (right + left < left + right)
                )
            )
        )
        result = "".join(values)
        return "0" if result[0] == "0" else result
