class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "").upper()
        first = len(chars) % k
        parts = ([chars[:first]] if first else []) + [
            chars[i : i + k] for i in range(first, len(chars), k)
        ]
        return "-".join(parts)
