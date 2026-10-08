class Solution:
    def numWays(self, s: str) -> int:
        modulus = 1_000_000_007
        one_positions = [index for index, char in enumerate(s) if char == "1"]
        ones = len(one_positions)
        if ones % 3:
            return 0
        if ones == 0:
            gaps = len(s) - 1
            return gaps * (gaps - 1) // 2 % modulus
        per_part = ones // 3
        first_choices = one_positions[per_part] - one_positions[per_part - 1]
        second_choices = one_positions[2 * per_part] - one_positions[2 * per_part - 1]
        return first_choices * second_choices % modulus
