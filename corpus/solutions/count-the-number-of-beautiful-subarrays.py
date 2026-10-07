class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        frequencies = defaultdict(int)
        frequencies[0] = 1
        prefix = 0
        answer = 0
        for value in nums:
            prefix ^= value
            answer += frequencies[prefix]
            frequencies[prefix] += 1
        return answer
