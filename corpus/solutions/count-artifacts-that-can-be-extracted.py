class Solution:
    def digArtifacts(
        self, n: int, artifacts: List[List[int]], dig: List[List[int]]
    ) -> int:
        excavated = {tuple(cell) for cell in dig}
        extracted = 0
        for top, left, bottom, right in artifacts:
            if all(
                (row, column) in excavated
                for row in range(top, bottom + 1)
                for column in range(left, right + 1)
            ):
                extracted += 1
        return extracted
