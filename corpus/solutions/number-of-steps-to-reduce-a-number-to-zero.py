class Solution:
    def numberOfSteps(self, num: int) -> int:
        return num.bit_length() + num.bit_count() - 1 if num else 0
