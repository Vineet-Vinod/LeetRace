class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_masks = {
            sum(1 << (ord(char) - ord("a")) for char in word) for word in startWords
        }
        possible = 0
        for word in targetWords:
            target_mask = sum(1 << (ord(char) - ord("a")) for char in word)
            bits = target_mask
            while bits:
                bit = bits & -bits
                if target_mask ^ bit in start_masks:
                    possible += 1
                    break
                bits ^= bit
        return possible
