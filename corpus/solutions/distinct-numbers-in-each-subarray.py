class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        answer = []
        for index, value in enumerate(nums):
            counts[value] += 1
            if index >= k:
                outgoing = nums[index - k]
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]
            if index >= k - 1:
                answer.append(len(counts))
        return answer
