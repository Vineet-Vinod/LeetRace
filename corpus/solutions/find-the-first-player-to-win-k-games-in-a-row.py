class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        champion = 0
        wins = 0
        for challenger in range(1, len(skills)):
            if skills[challenger] > skills[champion]:
                champion = challenger
                wins = 0
            wins += 1
            if wins == k:
                return champion
        return champion
