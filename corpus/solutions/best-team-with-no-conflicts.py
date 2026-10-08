class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        players = sorted(zip(ages, scores))
        best = [0] * len(players)
        answer = 0
        for index, (_, score) in enumerate(players):
            best[index] = score
            for previous in range(index):
                if players[previous][1] <= score:
                    best[index] = max(best[index], best[previous] + score)
            answer = max(answer, best[index])
        return answer
