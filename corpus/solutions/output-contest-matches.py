class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i) for i in range(1, n + 1)]
        while len(teams) > 1:
            teams = [f"({teams[i]},{teams[-1 - i]})" for i in range(len(teams) // 2)]
        return teams[0]
