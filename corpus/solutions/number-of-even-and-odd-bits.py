class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bits = bin(n)[2:][::-1]
        return [
            sum(bit == "1" for bit in bits[::2]),
            sum(bit == "1" for bit in bits[1::2]),
        ]
