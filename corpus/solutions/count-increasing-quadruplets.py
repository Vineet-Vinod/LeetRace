class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        triples = [0] * len(nums)
        answer = 0
        for last, value in enumerate(nums):
            smaller = 0
            for middle in range(last):
                if nums[middle] < value:
                    answer += triples[middle]
                    smaller += 1
                else:
                    triples[middle] += smaller
        return answer
