from typing import List


class Solution:
    def canAliceWin(self, a: List[str], b: List[str]) -> bool:
        losing = [[0] * 27 for _ in range(2)]
        i, j = len(a) - 1, len(b) - 1
        alice_wins = False
        while i >= 0 or j >= 0:
            if j < 0 or (i >= 0 and a[i] > b[j]):
                word, owner = a[i], 0
                i -= 1
            else:
                word, owner = b[j], 1
                j -= 1
            letter = ord(word[0]) - 97
            next_player_wins = (
                losing[1 - owner][letter] + losing[1 - owner][letter + 1] > 0
            )
            if not next_player_wins:
                losing[owner][letter] += 1
            if owner == 0 and i == -1:
                alice_wins = not next_player_wins
        return alice_wins
