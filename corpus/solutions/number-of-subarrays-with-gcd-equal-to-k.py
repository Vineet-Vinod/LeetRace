class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        answer = 0
        for start in range(len(nums)):
            common = 0
            for end in range(start, len(nums)):
                common = gcd(common, nums[end])
                if common == k:
                    answer += 1
                if common < k or common % k != 0:
                    break
        return answer
