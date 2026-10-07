class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        answer = 0
        while n:
            answer ^= n
            n >>= 1
        return answer
