class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        results = [
            currentState[:i] + "--" + currentState[i + 2 :]
            for i in range(len(currentState) - 1)
            if currentState[i : i + 2] == "++"
        ]
        return sorted(results)
