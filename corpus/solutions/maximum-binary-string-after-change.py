class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        zero_count = binary.count("0")
        if zero_count <= 1:
            return binary
        first_zero = binary.index("0")
        one_position = first_zero + zero_count - 1
        return "1" * one_position + "0" + "1" * (len(binary) - one_position - 1)
