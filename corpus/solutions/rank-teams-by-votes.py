class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""
        n = len(votes[0])
        counts = {ch: [0] * n for ch in votes[0]}
        for vote in votes:
            for i, ch in enumerate(vote):
                counts[ch][i] += 1
        return "".join(
            sorted(counts, key=lambda ch: (tuple(-x for x in counts[ch]), ch))
        )
