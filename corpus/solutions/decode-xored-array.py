class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for value in encoded:
            result.append(result[-1] ^ value)
        return result
