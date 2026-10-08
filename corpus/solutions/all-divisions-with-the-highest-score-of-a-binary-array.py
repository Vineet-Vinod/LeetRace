class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        left_zeros = 0
        best = -1
        answer: list[int] = []
        for i in range(len(nums) + 1):
            score = left_zeros + ones
            if score > best:
                best = score
                answer = [i]
            elif score == best:
                answer.append(i)
            if i < len(nums):
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    ones -= 1
        return answer
