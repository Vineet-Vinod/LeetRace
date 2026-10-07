class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        rank = [[0] * n for _ in range(n)]
        for person in range(n):
            for position, friend in enumerate(preferences[person]):
                rank[person][friend] = position
        partner = [-1] * n
        for a, b in pairs:
            partner[a], partner[b] = b, a
        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x][: rank[x][y]]:
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break
        return unhappy
