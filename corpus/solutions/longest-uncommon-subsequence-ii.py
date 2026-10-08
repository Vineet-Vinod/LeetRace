class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        ordered = sorted(
            enumerate(strs), key=lambda item: (-len(item[1]), item[1], item[0])
        )

        def is_subsequence(shorter: str, longer: str) -> bool:
            index = 0
            for char in longer:
                if index < len(shorter) and shorter[index] == char:
                    index += 1
            return index == len(shorter)

        for index, candidate in ordered:
            if all(
                index == other_index or not is_subsequence(candidate, other)
                for other_index, other in enumerate(strs)
            ):
                return len(candidate)
        return -1
