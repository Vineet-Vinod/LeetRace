class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = [0] * k
        counts[0] = 1
        prefix = answer = 0
        for value in nums:
            prefix = (prefix + value) % k
            answer += counts[prefix]
            counts[prefix] += 1
        return answer
