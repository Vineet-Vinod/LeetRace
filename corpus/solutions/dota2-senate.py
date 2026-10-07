class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        for index, party in enumerate(senate):
            (radiant if party == "R" else dire).append(index)
        size = len(senate)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + size)
            else:
                dire.append(d + size)
        return "Radiant" if radiant else "Dire"
