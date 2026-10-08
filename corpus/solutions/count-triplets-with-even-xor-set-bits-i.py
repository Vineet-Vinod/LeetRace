class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        return sum((x ^ y ^ z).bit_count() % 2 == 0 for x in a for y in b for z in c)
