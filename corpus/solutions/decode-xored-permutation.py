class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        size = len(encoded) + 1
        total = 0
        for value in range(1, size + 1):
            total ^= value
        suffix_xor = 0
        for index in range(1, len(encoded), 2):
            suffix_xor ^= encoded[index]
        first = total ^ suffix_xor
        permutation = [first]
        for value in encoded:
            permutation.append(permutation[-1] ^ value)
        return permutation
