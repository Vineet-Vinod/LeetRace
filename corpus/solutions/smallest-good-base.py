class Solution:
    def smallestGoodBase(self, n: str) -> str:
        number = int(n)
        for length in range(number.bit_length(), 2, -1):
            low, high = 2, 1 << ((number.bit_length() + length - 2) // (length - 1))
            while low <= high:
                base = (low + high) // 2
                value = 1
                for _ in range(length - 1):
                    value = value * base + 1
                    if value > number:
                        break
                if value == number:
                    return str(base)
                if value < number:
                    low = base + 1
                else:
                    high = base - 1
        return str(number - 1)
