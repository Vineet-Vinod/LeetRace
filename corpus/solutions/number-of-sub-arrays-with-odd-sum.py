class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        even = 1
        odd = answer = 0
        parity = 0
        for value in arr:
            parity ^= value & 1
            if parity:
                answer += even
                odd += 1
            else:
                answer += odd
                even += 1
        return answer % (10**9 + 7)
