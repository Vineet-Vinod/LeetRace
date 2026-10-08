class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        first_positions: dict[str, list[int]] = {}
        second_positions: dict[str, list[int]] = {}
        for index, char in enumerate(firstString):
            first_positions.setdefault(char, []).append(index)
        for index, char in enumerate(secondString):
            second_positions.setdefault(char, []).append(index)
        differences = [
            first_positions[char][0] - second_positions[char][-1]
            for char in first_positions.keys() & second_positions.keys()
        ]
        return (
            sum(difference == min(differences) for difference in differences)
            if differences
            else 0
        )
