class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(value: str) -> Tuple[int, int]:
            real, imaginary = value[:-1].split("+")
            return int(real), int(imaginary)

        a, b = parse(num1)
        c, d = parse(num2)
        return f"{a * c - b * d}+{a * d + b * c}i"
