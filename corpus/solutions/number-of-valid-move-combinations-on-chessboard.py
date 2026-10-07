from typing import List


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        straight = ((1, 0), (-1, 0), (0, 1), (0, -1))
        diagonal = ((1, 1), (1, -1), (-1, 1), (-1, -1))
        paths: list[list[tuple[tuple[int, int], ...]]] = []
        for piece, (r, c) in zip(pieces, positions):
            options = [((r, c),) * 8]
            directions = (
                straight
                if piece == "rook"
                else diagonal
                if piece == "bishop"
                else straight + diagonal
            )
            for dr, dc in directions:
                for steps in range(1, 8):
                    if not (1 <= r + dr * steps <= 8 and 1 <= c + dc * steps <= 8):
                        break
                    options.append(
                        tuple(
                            (r + dr * min(t, steps), c + dc * min(t, steps))
                            for t in range(8)
                        )
                    )
            paths.append(options)
        n = len(pieces)
        compatible: dict[tuple[int, int], list[int]] = {}
        for i in range(n):
            for j in range(i + 1, n):
                compatible[i, j] = [
                    sum(
                        1 << b
                        for b, other in enumerate(paths[j])
                        if all(x != y for x, y in zip(path, other))
                    )
                    for path in paths[i]
                ]

        def count(index: int, masks: List[int]) -> int:
            if index == n - 1:
                return masks[index].bit_count()
            answer = 0
            choices = masks[index]
            while choices:
                bit = choices & -choices
                choices -= bit
                option = bit.bit_length() - 1
                next_masks = masks[:]
                for j in range(index + 1, n):
                    next_masks[j] &= compatible[index, j][option]
                answer += count(index + 1, next_masks)
            return answer

        return count(0, [(1 << len(options)) - 1 for options in paths])
