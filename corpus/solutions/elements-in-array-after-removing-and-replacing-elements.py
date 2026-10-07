class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        answer: list[int] = []
        for time, index in queries:
            phase = time % (2 * n)
            if phase < n:
                answer.append(nums[phase + index] if phase + index < n else -1)
            else:
                restored = phase - n
                answer.append(nums[index] if index < restored else -1)
        return answer
