class Solution:
    def checkRecord(self, n: int) -> int:
        modulus = 1000000007
        matrix = [[0] * 6 for _ in range(6)]
        for a in range(2):
            for late in range(3):
                source = a * 3 + late
                matrix[a * 3][source] += 1
                if late < 2:
                    matrix[source + 1][source] += 1
                if a == 0:
                    matrix[3][source] += 1
        state = [1, 0, 0, 0, 0, 0]
        while n:
            if n & 1:
                state = [
                    sum(matrix[i][j] * state[j] for j in range(6)) % modulus
                    for i in range(6)
                ]
            matrix = [
                [
                    sum(matrix[i][k] * matrix[k][j] for k in range(6)) % modulus
                    for j in range(6)
                ]
                for i in range(6)
            ]
            n //= 2
        return sum(state) % modulus
