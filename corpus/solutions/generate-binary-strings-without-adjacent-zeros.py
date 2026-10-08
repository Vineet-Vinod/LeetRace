class Solution:
    def validStrings(self, n: int) -> List[str]:
        return [
            format(value, f"0{n}b")
            for value in range(1 << n)
            if "00" not in format(value, f"0{n}b")
        ]
