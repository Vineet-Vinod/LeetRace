class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()
        common = 0
        result = []
        for a, b in zip(A, B):
            seen_a.add(a)
            seen_b.add(b)
            common = len(seen_a & seen_b)
            result.append(common)
        return result
