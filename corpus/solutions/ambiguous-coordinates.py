class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        digits = s[1:-1]

        def numbers(part: str) -> List[str]:
            out = []
            if part == "0" or not part.startswith("0"):
                out.append(part)
            for i in range(1, len(part)):
                left, right = part[:i], part[i:]
                if (left == "0" or not left.startswith("0")) and not right.endswith(
                    "0"
                ):
                    out.append(left + "." + right)
            return out

        result = []
        for split in range(1, len(digits)):
            for left in numbers(digits[:split]):
                for right in numbers(digits[split:]):
                    result.append(f"({left}, {right})")
        return sorted(result)
