class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        values = sorted(nums)
        answers: list[list[int]] = []
        for i in range(len(values) - 2):
            if i and values[i] == values[i - 1]:
                continue
            left, right = i + 1, len(values) - 1
            while left < right:
                total = values[i] + values[left] + values[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    answers.append([values[i], values[left], values[right]])
                    left += 1
                    right -= 1
                    while left < right and values[left] == values[left - 1]:
                        left += 1
                    while left < right and values[right] == values[right + 1]:
                        right -= 1
        return answers
