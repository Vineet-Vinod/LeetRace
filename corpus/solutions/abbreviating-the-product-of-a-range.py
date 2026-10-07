import sys

sys.set_int_max_str_digits(0)


class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        product = 1
        for x in range(left, right + 1):
            product *= x
        zeros = 0
        while product % 10 == 0:
            product //= 10
            zeros += 1
        digits = str(product)
        if len(digits) > 10:
            digits = digits[:5] + "..." + digits[-5:]
        return digits + "e" + str(zeros)
