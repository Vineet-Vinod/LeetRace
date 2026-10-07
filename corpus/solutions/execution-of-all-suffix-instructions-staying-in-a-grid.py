class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        answer: list[int] = []
        for start in range(len(s)):
            row, col = startPos
            count = 0
            for instruction in s[start:]:
                if instruction == "L":
                    col -= 1
                elif instruction == "R":
                    col += 1
                elif instruction == "U":
                    row -= 1
                else:
                    row += 1
                if not (0 <= row < n and 0 <= col < n):
                    break
                count += 1
            answer.append(count)
        return answer
