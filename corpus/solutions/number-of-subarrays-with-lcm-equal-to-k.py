class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        answer = 0
        for start in range(len(nums)):
            current = 1
            for end in range(start, len(nums)):
                if k % nums[end] != 0:
                    break
                current = math.lcm(current, nums[end])
                if current == k:
                    answer += 1
                elif current > k:
                    break
        return answer
