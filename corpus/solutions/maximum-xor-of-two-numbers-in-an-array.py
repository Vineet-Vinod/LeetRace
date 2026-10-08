class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer = 0
        for bit in range(30, -1, -1):
            answer <<= 1
            prefixes = {value >> bit for value in nums}
            candidate = answer | 1
            if any(candidate ^ prefix in prefixes for prefix in prefixes):
                answer = candidate
        return answer
