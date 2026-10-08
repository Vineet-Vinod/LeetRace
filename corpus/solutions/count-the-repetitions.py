class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2) <= set(s1):
            return 0
        seen: dict[int, tuple[int, int]] = {}
        block = matched = index = 0
        while block < n1:
            if index in seen:
                old_block, old_matched = seen[index]
                repeats = (n1 - block) // (block - old_block)
                if repeats:
                    matched += repeats * (matched - old_matched)
                    block += repeats * (block - old_block)
                    seen.clear()
                    continue
            seen[index] = (block, matched)
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        matched += 1
                        index = 0
            block += 1
        return matched // n2
