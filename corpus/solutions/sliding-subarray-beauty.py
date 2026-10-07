class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        counts = [0] * 101
        answer = []
        for right, value in enumerate(nums):
            counts[value + 50] += 1
            if right >= k:
                counts[nums[right - k] + 50] -= 1
            if right >= k - 1:
                remaining = x
                beauty = 0
                for value in range(-50, 0):
                    remaining -= counts[value + 50]
                    if remaining <= 0:
                        beauty = value
                        break
                answer.append(beauty)
        return answer
