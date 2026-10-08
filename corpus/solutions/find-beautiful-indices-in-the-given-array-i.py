class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(pattern: str) -> List[int]:
            positions: List[int] = []
            start = 0
            while True:
                found = s.find(pattern, start)
                if found < 0:
                    return positions
                positions.append(found)
                start = found + 1

        a_positions = occurrences(a)
        b_positions = occurrences(b)
        return [
            index
            for index in a_positions
            if (pos := bisect_left(b_positions, index - k)) < len(b_positions)
            and b_positions[pos] <= index + k
        ]
