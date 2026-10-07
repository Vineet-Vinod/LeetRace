class Solution:
    def findIntegers(self, n: int) -> int:
        counts = [1, 2]
        for _ in range(2, n.bit_length() + 1):
            counts.append(counts[-1] + counts[-2])
        answer, previous = 0, 0
        for bit in range(n.bit_length() - 1, -1, -1):
            if n & (1 << bit):
                answer += counts[bit]
                if previous:
                    return answer
                previous = 1
            else:
                previous = 0
        return answer + 1
