class Solution:
    def binaryGap(self, n: int) -> int:
        last_one = -1
        answer = 0
        bit_index = 0
        while n:
            if n & 1:
                if last_one >= 0:
                    answer = max(answer, bit_index - last_one)
                last_one = bit_index
            n >>= 1
            bit_index += 1
        return answer
