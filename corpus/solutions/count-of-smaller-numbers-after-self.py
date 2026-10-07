from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        values = {value: i + 1 for i, value in enumerate(sorted(set(nums)))}
        bit = [0] * (len(values) + 1)
        answer = []
        for value in reversed(nums):
            index = values[value] - 1
            count = 0
            while index:
                count += bit[index]
                index -= index & -index
            answer.append(count)
            index = values[value]
            while index < len(bit):
                bit[index] += 1
                index += index & -index
        return answer[::-1]
