class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        frequencies = defaultdict(int)
        frequencies[0] = 1
        prefix = 0
        answer = 0
        for value in nums:
            if value % modulo == k:
                prefix += 1
            answer += frequencies[(prefix - k) % modulo]
            frequencies[prefix % modulo] += 1
        return answer
