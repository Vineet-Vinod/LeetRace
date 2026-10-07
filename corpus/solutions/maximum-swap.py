class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_position = {digit: index for index, digit in enumerate(digits)}
        for index, digit in enumerate(digits):
            for larger in "9876543210":
                if (
                    larger > digit
                    and larger in last_position
                    and last_position[larger] > index
                ):
                    other = last_position[larger]
                    digits[index], digits[other] = digits[other], digits[index]
                    return int("".join(digits))
        return num
