class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped(number: int) -> int:
            digits = str(number)
            return int("".join(str(mapping[int(digit)]) for digit in digits))

        return sorted(nums, key=mapped)
